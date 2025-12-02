"""
transfer_from_aws_to_gcp.py

Complete migration script that:
1. Reads all tables from AWS RDS
2. Extracts complete schema (tables, columns, constraints, indexes)
3. Creates tables in GCP if they don't exist
4. Transfers all data from AWS to GCP

Environment variables required:
    - AWS_DB_HOST, AWS_DB_PORT (optional, default 5432), AWS_DB_NAME, AWS_DB_USER, AWS_DB_PASSWORD
    - DEST_AWS_DB_HOST, DEST_AWS_DB_PORT (optional, default 5432), DEST_AWS_DB_NAME, DEST_AWS_DB_USER, DEST_AWS_DB_PASSWORD
"""

import os
import sys
import json
import time
from dotenv import load_dotenv
import psycopg2
import psycopg2.extras
from psycopg2 import sql
from psycopg2.extras import Json

# Load environment variables
load_dotenv()


def getenv_or_exit(name, example=None):
    val = os.environ.get(name)
    if not val:
        sys.stderr.write(f"Environment variable {name} is not set.\n")
        if example:
            sys.stderr.write(f"Example (bash): export {name}={example}\n")
        sys.exit(1)
    return val


# Store connection parameters for reconnection
AWS_CONN_PARAMS = {
    'host': None,
    'port': None,
    'dbname': None,
    'user': None,
    'password': None
}

DEST_AWS_CONN_PARAMS = {
    'host': None,
    'port': None,
    'dbname': None,
    'user': None,
    'password': None,
    'sslmode': 'disable'
}

# Global connection objects
aws_conn = None
dest_aws_conn = None
aws_cur = None
dest_aws_cur = None


# ----------------------------------------
# CONNECTION MANAGEMENT
# ----------------------------------------
def connect_aws():
    global aws_conn, aws_cur
    try:
        if aws_conn and not aws_conn.closed:
            aws_conn.close()
    except:
        pass
    
    aws_conn = psycopg2.connect(**AWS_CONN_PARAMS)
    aws_conn.autocommit = False
    aws_cur = aws_conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    return aws_conn, aws_cur


def connect_dest_aws():
    global dest_aws_conn, dest_aws_cur
    try:
        if dest_aws_conn and not dest_aws_conn.closed:
            dest_aws_conn.close()
    except:
        pass
    
    dest_aws_conn = psycopg2.connect(**DEST_AWS_CONN_PARAMS)
    dest_aws_conn.autocommit = False
    dest_aws_cur = dest_aws_conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    return dest_aws_conn, dest_aws_cur

# Backwards-compatible aliases for older GCP-based variable names
# This keeps the rest of the script working without changing all references.
GCP_CONN_PARAMS = DEST_AWS_CONN_PARAMS

def connect_gcp():
    # create destination AWS connection but expose it under the old name
    conn, cur = connect_dest_aws()
    globals()['gcp_conn'] = conn
    globals()['gcp_cur'] = cur
    return conn, cur

def ensure_gcp_connection():
    # delegate to destination AWS ensure function and keep legacy names in sync
    ensure_dest_aws_connection()
    globals()['gcp_conn'] = globals().get('dest_aws_conn')
    globals()['gcp_cur'] = globals().get('dest_aws_cur')


def ensure_aws_connection():
    global aws_conn, aws_cur
    try:
        if aws_conn.closed or aws_cur.closed:
            print("  🔄 Reconnecting to AWS...")
            connect_aws()
    except:
        print("  🔄 Reconnecting to AWS...")
        connect_aws()


def ensure_dest_aws_connection():
    global dest_aws_conn, dest_aws_cur
    try:
        if dest_aws_conn.closed or dest_aws_cur.closed:
            print("  🔄 Reconnecting to destination AWS...")
            connect_dest_aws()
    except:
        print("  🔄 Reconnecting to destination AWS...")
        connect_dest_aws()


# ----------------------------------------
# INITIALIZE CONNECTIONS
# ----------------------------------------
print("🔌 Connecting to databases...")

AWS_CONN_PARAMS['host'] = getenv_or_exit("AWS_DB_HOST")
AWS_CONN_PARAMS['port'] = os.environ.get("AWS_DB_PORT", "5432")
AWS_CONN_PARAMS['dbname'] = getenv_or_exit("AWS_DB_NAME")
AWS_CONN_PARAMS['user'] = getenv_or_exit("AWS_DB_USER")
AWS_CONN_PARAMS['password'] = getenv_or_exit("AWS_DB_PASSWORD")

DEST_AWS_CONN_PARAMS['host'] = getenv_or_exit("DEST_AWS_DB_HOST")
DEST_AWS_CONN_PARAMS['port'] = os.environ.get("DEST_AWS_DB_PORT", "5432")
DEST_AWS_CONN_PARAMS['dbname'] = getenv_or_exit("DEST_AWS_DB_NAME")
DEST_AWS_CONN_PARAMS['user'] = getenv_or_exit("DEST_AWS_DB_USER")
DEST_AWS_CONN_PARAMS['password'] = getenv_or_exit("DEST_AWS_DB_PASSWORD")

try:
    connect_aws()
    print("✅ Connected to AWS")
except Exception as e:
    sys.stderr.write(f"Failed to connect to AWS Postgres: {e}\n")
    sys.exit(1)

try:
    conn, cur = connect_dest_aws()
    # keep legacy names in sync
    globals()['gcp_conn'] = conn
    globals()['gcp_cur'] = cur
    print("✅ Connected to destination AWS")
except Exception as e:
    sys.stderr.write(f"Failed to connect to destination AWS Postgres: {e}\n")
    sys.exit(1)

# Enable required extensions in GCP
print("🔧 Enabling required PostgreSQL extensions on destination...")
try:
    dest_aws_cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
    dest_aws_conn.commit()
    print("✅ uuid-ossp extension enabled on destination")
except Exception as e:
    print(f"⚠️ Could not enable uuid-ossp extension on destination: {e}")
    dest_aws_conn.rollback()


# ----------------------------------------
# Function to sanitize each row
# ----------------------------------------
def sanitize_row(row: dict):
    cleaned = []
    for value in row.values():
        if isinstance(value, dict):
            cleaned.append(Json(value))
        elif isinstance(value, list):
            # Handle lists - convert to PostgreSQL array format
            cleaned.append(value)
        elif isinstance(value, str):
            # Check if string looks like a JSON array but should be a PostgreSQL array
            if value.startswith('[') and value.endswith(']'):
                try:
                    # Try to parse as JSON
                    parsed = json.loads(value)
                    if isinstance(parsed, list):
                        # It's a JSON array - keep as list for PostgreSQL array columns
                        cleaned.append(parsed)
                    else:
                        cleaned.append(value)
                except (json.JSONDecodeError, ValueError):
                    # Not valid JSON, keep as string
                    cleaned.append(value)
            else:
                cleaned.append(value)
        else:
            cleaned.append(value)
    return cleaned


# ----------------------------------------
# GET ALL TABLES FROM AWS
# ----------------------------------------
def get_aws_tables():
    print("📋 Fetching tables from AWS...")
    ensure_aws_connection()
    aws_cur.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public' 
          AND table_type = 'BASE TABLE'
        ORDER BY table_name;
    """)
    tables = [row['table_name'] for row in aws_cur.fetchall()]
    print(f"✅ Found {len(tables)} tables")
    return tables


# ----------------------------------------
# ANALYZE TABLE DEPENDENCIES
# ----------------------------------------
def get_table_dependencies():
    """Get foreign key dependencies to determine transfer order"""
    ensure_aws_connection()
    aws_cur.execute("""
        SELECT 
            tc.table_name,
            ccu.table_name AS foreign_table_name
        FROM information_schema.table_constraints AS tc
        JOIN information_schema.constraint_column_usage AS ccu
          ON ccu.constraint_name = tc.constraint_name
          AND ccu.table_schema = tc.table_schema
        WHERE tc.constraint_type = 'FOREIGN KEY'
          AND tc.table_schema = 'public'
        ORDER BY tc.table_name;
    """)
    
    dependencies = {}
    for row in aws_cur.fetchall():
        table = row['table_name']
        foreign_table = row['foreign_table_name']
        if table not in dependencies:
            dependencies[table] = set()
        if foreign_table != table:  # Ignore self-references
            dependencies[table].add(foreign_table)
    
    return dependencies


# ----------------------------------------
# TOPOLOGICAL SORT FOR TABLE ORDER
# ----------------------------------------
def topological_sort_tables(tables, dependencies):
    """Sort tables based on foreign key dependencies"""
    # Tables with no dependencies
    no_deps = [t for t in tables if t not in dependencies or not dependencies[t]]
    
    # Tables with dependencies
    with_deps = [t for t in tables if t in dependencies and dependencies[t]]
    
    sorted_tables = []
    sorted_tables.extend(no_deps)
    
    # Simple approach: keep trying to add tables whose dependencies are met
    max_iterations = len(with_deps) * 2
    iteration = 0
    
    while with_deps and iteration < max_iterations:
        iteration += 1
        tables_added = []
        
        for table in with_deps:
            # Check if all dependencies are already in sorted list
            if all(dep in sorted_tables for dep in dependencies[table]):
                sorted_tables.append(table)
                tables_added.append(table)
        
        # Remove added tables from with_deps
        for table in tables_added:
            with_deps.remove(table)
    
    # Add remaining tables (circular dependencies or issues)
    sorted_tables.extend(with_deps)
    
    return sorted_tables
def get_aws_enums():
    print("📋 Fetching ENUM types from AWS...")
    ensure_aws_connection()
    aws_cur.execute("""
        SELECT 
            t.typname as enum_name,
            array_agg(e.enumlabel ORDER BY e.enumsortorder) as enum_values
        FROM pg_type t
        JOIN pg_enum e ON t.oid = e.enumtypid
        JOIN pg_catalog.pg_namespace n ON n.oid = t.typnamespace
        WHERE n.nspname = 'public'
        GROUP BY t.typname
        ORDER BY t.typname;
    """)
    enums = aws_cur.fetchall()
    print(f"✅ Found {len(enums)} ENUM types")
    return enums


# ----------------------------------------
# CREATE ENUM TYPES IN GCP
# ----------------------------------------
def create_enum_type(enum_name, enum_values):
    ensure_gcp_connection()
    # Check if enum already exists
    gcp_cur.execute("""
        SELECT EXISTS (
            SELECT 1 
            FROM pg_type t
            JOIN pg_catalog.pg_namespace n ON n.oid = t.typnamespace
            WHERE t.typname = %s 
              AND n.nspname = 'public'
        );
    """, (enum_name,))
    
    if gcp_cur.fetchone()['exists']:
        print(f"  ⏭️  ENUM {enum_name} already exists, skipping...")
        return True
    
    try:
        # Create the enum type
        values_str = ', '.join([f"'{val}'" for val in enum_values])
        create_enum_sql = f"CREATE TYPE {enum_name} AS ENUM ({values_str});"
        gcp_cur.execute(create_enum_sql)
        gcp_conn.commit()
        print(f"  ✅ Created ENUM: {enum_name}")
        return True
    except Exception as e:
        print(f"  ❌ Error creating ENUM {enum_name}: {e}")
        gcp_conn.rollback()
        return False


# ----------------------------------------
# GET TABLE SCHEMA FROM AWS
# ----------------------------------------
def get_table_schema(table_name):
    print(f"📐 Extracting schema for table: {table_name}")
    ensure_aws_connection()
    
    # Get column definitions with UDT name for arrays
    aws_cur.execute("""
        SELECT 
            column_name,
            data_type,
            udt_name,
            character_maximum_length,
            numeric_precision,
            numeric_scale,
            is_nullable,
            column_default
        FROM information_schema.columns
        WHERE table_schema = 'public' 
          AND table_name = %s
        ORDER BY ordinal_position;
    """, (table_name,))
    
    columns = aws_cur.fetchall()
    
    # Get primary key
    aws_cur.execute("""
        SELECT a.attname AS column_name
        FROM pg_index i
        JOIN pg_attribute a ON a.attrelid = i.indrelid 
                            AND a.attnum = ANY(i.indkey)
        WHERE i.indrelid = %s::regclass
          AND i.indisprimary;
    """, (table_name,))
    
    pk_columns = [row['column_name'] for row in aws_cur.fetchall()]
    
    # Get foreign keys
    aws_cur.execute("""
        SELECT
            tc.constraint_name,
            kcu.column_name,
            ccu.table_name AS foreign_table_name,
            ccu.column_name AS foreign_column_name
        FROM information_schema.table_constraints AS tc
        JOIN information_schema.key_column_usage AS kcu
          ON tc.constraint_name = kcu.constraint_name
          AND tc.table_schema = kcu.table_schema
        JOIN information_schema.constraint_column_usage AS ccu
          ON ccu.constraint_name = tc.constraint_name
          AND ccu.table_schema = tc.table_schema
        WHERE tc.constraint_type = 'FOREIGN KEY'
          AND tc.table_name = %s
          AND tc.table_schema = 'public';
    """, (table_name,))
    
    foreign_keys = aws_cur.fetchall()
    
    # Get unique constraints
    aws_cur.execute("""
        SELECT
            tc.constraint_name,
            kcu.column_name
        FROM information_schema.table_constraints AS tc
        JOIN information_schema.key_column_usage AS kcu
          ON tc.constraint_name = kcu.constraint_name
          AND tc.table_schema = kcu.table_schema
        WHERE tc.constraint_type = 'UNIQUE'
          AND tc.table_name = %s
          AND tc.table_schema = 'public';
    """, (table_name,))
    
    unique_constraints = aws_cur.fetchall()
    
    # Get indexes
    aws_cur.execute("""
        SELECT
            i.relname AS index_name,
            a.attname AS column_name,
            ix.indisunique AS is_unique
        FROM pg_class t
        JOIN pg_index ix ON t.oid = ix.indrelid
        JOIN pg_class i ON i.oid = ix.indexrelid
        JOIN pg_attribute a ON a.attrelid = t.oid 
                            AND a.attnum = ANY(ix.indkey)
        WHERE t.relname = %s
          AND t.relkind = 'r'
          AND NOT ix.indisprimary
        ORDER BY i.relname, a.attnum;
    """, (table_name,))
    
    indexes = aws_cur.fetchall()
    
    return {
        'columns': columns,
        'primary_keys': pk_columns,
        'foreign_keys': foreign_keys,
        'unique_constraints': unique_constraints,
        'indexes': indexes
    }


# ----------------------------------------
# BUILD CREATE TABLE STATEMENT
# ----------------------------------------
def build_create_table_sql(table_name, schema):
    col_defs = []
    sequences_needed = []
    
    # Quote table name if it's a reserved keyword
    safe_table_name = f'"{table_name}"' if table_name.lower() in ['user', 'group', 'order', 'table'] else table_name
    
    for col in schema['columns']:
        col_name = col['column_name']
        data_type = col['data_type']
        udt_name = col.get('udt_name', '')
        
        # Handle different data types
        if data_type == 'ARRAY':
            # Handle array types - extract base type from udt_name
            if udt_name.startswith('_'):
                base_type = udt_name[1:]  # Remove leading underscore
                if base_type == 'text':
                    col_type = "TEXT[]"
                elif base_type == 'varchar':
                    col_type = "VARCHAR[]"
                elif base_type == 'int4':
                    col_type = "INTEGER[]"
                elif base_type == 'int8':
                    col_type = "BIGINT[]"
                elif base_type == 'uuid':
                    col_type = "UUID[]"
                else:
                    col_type = f"{base_type.upper()}[]"
            else:
                col_type = "TEXT[]"  # Default fallback
        elif data_type == 'USER-DEFINED':
            # Check if it's an ENUM type or JSONB
            if udt_name in ['jsonb', 'json']:
                col_type = udt_name.upper()
            else:
                # It's likely an ENUM type - use the udt_name
                col_type = udt_name
        elif data_type == 'character varying':
            if col['character_maximum_length']:
                col_type = f"VARCHAR({col['character_maximum_length']})"
            else:
                col_type = "VARCHAR"
        elif data_type == 'character':
            col_type = f"CHAR({col['character_maximum_length']})"
        elif data_type == 'numeric':
            if col['numeric_precision'] and col['numeric_scale']:
                col_type = f"NUMERIC({col['numeric_precision']}, {col['numeric_scale']})"
            else:
                col_type = "NUMERIC"
        elif data_type == 'timestamp without time zone':
            col_type = "TIMESTAMP"
        elif data_type == 'timestamp with time zone':
            col_type = "TIMESTAMPTZ"
        else:
            col_type = data_type.upper()
        
        # Nullable constraint
        nullable = "" if col['is_nullable'] == 'YES' else " NOT NULL"
        
        # Default value - handle sequences
        default = ""
        if col['column_default']:
            default_val = col['column_default']
            
            # Handle nextval for sequences
            if 'nextval' in default_val:
                # Extract sequence name
                import re
                seq_match = re.search(r"nextval\('([^']+)'", default_val)
                if seq_match:
                    seq_name = seq_match.group(1).replace('::regclass', '').strip("'\"")
                    sequences_needed.append((seq_name, safe_table_name, col_name))
                    # Use SERIAL type instead
                    if col_type == "INTEGER":
                        col_type = "SERIAL"
                        nullable = ""
                        default = ""
                    elif col_type == "BIGINT":
                        col_type = "BIGSERIAL"
                        nullable = ""
                        default = ""
            else:
                default = f" DEFAULT {default_val}"
        
        col_defs.append(f'"{col_name}" {col_type}{nullable}{default}')
    
    # Add primary key
    if schema['primary_keys']:
        pk_cols = ', '.join([f'"{col}"' for col in schema['primary_keys']])
        col_defs.append(f"PRIMARY KEY ({pk_cols})")
    
    # Add unique constraints
    unique_dict = {}
    for uc in schema['unique_constraints']:
        constraint_name = uc['constraint_name']
        if constraint_name not in unique_dict:
            unique_dict[constraint_name] = []
        unique_dict[constraint_name].append(uc['column_name'])
    
    for constraint_name, columns in unique_dict.items():
        cols = ', '.join([f'"{col}"' for col in columns])
        col_defs.append(f"UNIQUE ({cols})")
    
    create_sql = f"CREATE TABLE IF NOT EXISTS {safe_table_name} (\n  "
    create_sql += ",\n  ".join(col_defs)
    create_sql += "\n);"
    
    return create_sql, sequences_needed


# ----------------------------------------
# CREATE INDEXES
# ----------------------------------------
def create_indexes(table_name, schema):
    ensure_gcp_connection()
    # Quote table name if it's a reserved keyword
    safe_table_name = f'"{table_name}"' if table_name.lower() in ['user', 'group', 'order', 'table'] else table_name
    
    index_dict = {}
    for idx in schema['indexes']:
        idx_name = idx['index_name']
        if idx_name not in index_dict:
            index_dict[idx_name] = {
                'columns': [],
                'is_unique': idx['is_unique']
            }
        index_dict[idx_name]['columns'].append(idx['column_name'])
    
    for idx_name, idx_info in index_dict.items():
        cols = ', '.join([f'"{col}"' for col in idx_info['columns']])
        unique = "UNIQUE " if idx_info['is_unique'] else ""
        
        try:
            create_idx_sql = f"CREATE {unique}INDEX IF NOT EXISTS {idx_name} ON {safe_table_name} ({cols});"
            gcp_cur.execute(create_idx_sql)
            print(f"  ✅ Created index: {idx_name}")
        except Exception as e:
            print(f"  ⚠️ Could not create index {idx_name}: {e}")


# ----------------------------------------
# CREATE FOREIGN KEYS (after all tables created)
# ----------------------------------------
def create_foreign_keys(table_name, schema):
    ensure_gcp_connection()
    # Quote table name if it's a reserved keyword
    safe_table_name = f'"{table_name}"' if table_name.lower() in ['user', 'group', 'order', 'table'] else table_name
    
    for fk in schema['foreign_keys']:
        constraint_name = fk['constraint_name']
        column_name = fk['column_name']
        foreign_table = fk['foreign_table_name']
        foreign_column = fk['foreign_column_name']
        
        # Quote foreign table if needed
        safe_foreign_table = f'"{foreign_table}"' if foreign_table.lower() in ['user', 'group', 'order', 'table'] else foreign_table
        
        try:
            fk_sql = f"""
                ALTER TABLE {safe_table_name} 
                ADD CONSTRAINT {constraint_name} 
                FOREIGN KEY ("{column_name}") 
                REFERENCES {safe_foreign_table}("{foreign_column}");
            """
            gcp_cur.execute(fk_sql)
            print(f"  ✅ Created foreign key: {constraint_name}")
        except Exception as e:
            print(f"  ⚠️ Could not create foreign key {constraint_name}: {e}")


# ----------------------------------------
# CHECK IF TABLE EXISTS IN GCP
# ----------------------------------------
def table_exists_in_gcp(table_name):
    ensure_gcp_connection()
    gcp_cur.execute("""
        SELECT EXISTS (
            SELECT 1 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
              AND table_name = %s
        );
    """, (table_name,))
    return gcp_cur.fetchone()['exists']


# ----------------------------------------
# CHECK IF TABLE HAS DATA IN GCP
# ----------------------------------------
def get_row_counts(table_name):
    """Get row counts from both AWS and GCP"""
    try:
        ensure_aws_connection()
        aws_cur.execute(sql.SQL("SELECT COUNT(*) as count FROM {}").format(sql.Identifier(table_name)))
        aws_count = aws_cur.fetchone()['count']
    except Exception as e:
        print(f"  ⚠️ Error getting AWS count for {table_name}: {e}")
        aws_count = 0
    
    try:
        ensure_gcp_connection()
        gcp_cur.execute(sql.SQL("SELECT COUNT(*) as count FROM {}").format(sql.Identifier(table_name)))
        gcp_count = gcp_cur.fetchone()['count']
    except Exception as e:
        print(f"  ⚠️ Error getting GCP count for {table_name}: {e}")
        gcp_count = 0
    
    return aws_count, gcp_count


# ----------------------------------------
# TRANSFER DATA WITH RETRY LOGIC
# ----------------------------------------
def transfer_data(table_name, max_retries=3, force_transfer=False):
    print(f"📦 Transferring data for: {table_name}")
    
    # Quote table name if it's a reserved keyword
    safe_table_name = f'"{table_name}"' if table_name.lower() in ['user', 'group', 'order', 'table'] else table_name
    
    # Check row counts in both databases
    aws_count, gcp_count = get_row_counts(table_name)
    
    print(f"  📊 AWS: {aws_count} rows | GCP: {gcp_count} rows")
    
    # Skip if counts match (data already synced)
    if not force_transfer and aws_count == gcp_count and gcp_count > 0:
        print(f"  ✅ Row counts match, data already synced, skipping...")
        return True
    
    # Skip if GCP has more data than AWS (unusual case)
    if not force_transfer and gcp_count > aws_count:
        print(f"  ⚠️ GCP has MORE data than AWS ({gcp_count} > {aws_count}), skipping to prevent data loss...")
        print(f"     Use force_transfer=True if you want to overwrite")
        return False
    
    # If GCP has some data but less than AWS, we need to clear it first
    if gcp_count > 0 and gcp_count < aws_count:
        print(f"  ⚠️ GCP has {gcp_count} rows but AWS has {aws_count} rows")
        print(f"  🗑️  Clearing existing data in GCP to ensure consistency...")
        try:
            ensure_gcp_connection()
            gcp_cur.execute(sql.SQL("TRUNCATE TABLE {} CASCADE").format(sql.Identifier(table_name)))
            gcp_conn.commit()
            print(f"  ✅ Table cleared")
        except Exception as e:
            print(f"  ❌ Failed to clear table: {e}")
            gcp_conn.rollback()
            return False
    
    retry_count = 0
    while retry_count < max_retries:
        try:
            # Ensure fresh connections
            ensure_aws_connection()
            ensure_gcp_connection()
            
            # Fetch data from AWS
            print(f"  📥 Fetching data from AWS...")
            aws_cur.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name)))
            rows = aws_cur.fetchall()
            
            if not rows:
                print(f"  ⚠️ No rows in AWS table {table_name}")
                return True
            
            # Build insert statement with quoted identifiers
            columns = rows[0].keys()
            col_names = sql.SQL(', ').join([sql.Identifier(col) for col in columns])
            placeholders = sql.SQL(', ').join(sql.Placeholder() * len(columns))
            
            insert_query = sql.SQL("""
                INSERT INTO {} ({})
                VALUES ({})
            """).format(sql.Identifier(table_name), col_names, placeholders)
            
            # Insert all rows in smaller batches
            batch_size = 500
            total_rows = len(rows)
            inserted_count = 0
            
            print(f"  📤 Inserting {total_rows} rows into GCP...")
            
            for i in range(0, total_rows, batch_size):
                batch = rows[i:i+batch_size]
                
                for row in batch:
                    try:
                        ensure_gcp_connection()
                        gcp_cur.execute(insert_query, sanitize_row(row))
                        inserted_count += 1
                    except Exception as row_error:
                        print(f"  ⚠️ Error inserting row: {row_error}")
                        try:
                            gcp_conn.rollback()
                            ensure_gcp_connection()
                        except:
                            pass
                        continue
                
                try:
                    gcp_conn.commit()
                    print(f"  ✅ Inserted {min(i+batch_size, total_rows)}/{total_rows} rows")
                except Exception as commit_error:
                    print(f"  ⚠️ Commit error: {commit_error}")
                    gcp_conn.rollback()
            
            # Verify the counts match after transfer
            final_aws_count, final_gcp_count = get_row_counts(table_name)
            print(f"  📊 Final: AWS: {final_aws_count} rows | GCP: {final_gcp_count} rows")
            
            if final_aws_count == final_gcp_count:
                print(f"  ✅ SUCCESS: Data synced perfectly! ({final_gcp_count} rows)")
                return True
            else:
                print(f"  ⚠️ WARNING: Row count mismatch! AWS:{final_aws_count} != GCP:{final_gcp_count}")
                return False
            
        except Exception as e:
            retry_count += 1
            print(f"  ⚠️ Error transferring data (attempt {retry_count}/{max_retries}): {e}")
            
            if retry_count < max_retries:
                print(f"  🔄 Retrying in 2 seconds...")
                time.sleep(2)
                try:
                    connect_aws()
                    connect_gcp()
                except Exception as conn_error:
                    print(f"  ⚠️ Reconnection error: {conn_error}")
            else:
                print(f"  ❌ Failed to transfer data for {table_name} after {max_retries} attempts")
                return False
    
    return False


# ----------------------------------------
# MAIN MIGRATION PROCESS
# ----------------------------------------
def main():
    print("\n" + "="*60)
    print("🚀 AWS TO GCP POSTGRESQL MIGRATION")
    print("="*60 + "\n")
    
    # Step 0: Get and create ENUM types first
    print("\n" + "="*60)
    print("🎨 PHASE 0: CREATING ENUM TYPES")
    print("="*60 + "\n")
    
    enums = get_aws_enums()
    for enum in enums:
        enum_name = enum['enum_name']
        enum_values = enum['enum_values']
        create_enum_type(enum_name, enum_values)
    
    # Step 1: Get all tables
    tables = get_aws_tables()
    
    # Store schemas for all tables
    table_schemas = {}
    
    print("\n" + "="*60)
    print("📐 PHASE 1: EXTRACTING SCHEMAS")
    print("="*60 + "\n")
    
    for table_name in tables:
        schema = get_table_schema(table_name)
        table_schemas[table_name] = schema
    
    print("\n" + "="*60)
    print("🏗️  PHASE 2: CREATING TABLES IN GCP")
    print("="*60 + "\n")
    
    # Step 2: Create tables (without foreign keys first)
    all_sequences = []
    
    for table_name in tables:
        if table_exists_in_gcp(table_name):
            print(f"⏭️  Table {table_name} already exists in GCP, skipping creation...")
            continue
        
        schema = table_schemas[table_name]
        create_sql, sequences_needed = build_create_table_sql(table_name, schema)
        all_sequences.extend(sequences_needed)
        
        try:
            ensure_gcp_connection()
            print(f"🏗️  Creating table: {table_name}")
            gcp_cur.execute(create_sql)
            gcp_conn.commit()
            print(f"  ✅ Table created successfully")
            
            # Create indexes
            create_indexes(table_name, schema)
            gcp_conn.commit()
            
        except Exception as e:
            print(f"  ❌ Error creating table {table_name}: {e}")
            gcp_conn.rollback()
            continue
    
    print("\n" + "="*60)
    print("📦 PHASE 3: TRANSFERRING DATA")
    print("="*60 + "\n")
    
    print("ℹ️  Smart Sync Mode:")
    print("  • Skips tables where row counts already match")
    print("  • Clears and re-syncs tables with mismatched counts")
    print("  • Verifies data integrity after transfer\n")
    
    # Step 3: Transfer data with smart sync
    failed_tables = []
    skipped_tables = []
    synced_tables = []
    mismatch_tables = []
    
    for table_name in tables:
        try:
            result = transfer_data(table_name, force_transfer=False)
            
            if result is True:
                # Check if it was skipped or synced
                aws_count, gcp_count = get_row_counts(table_name)
                if aws_count == gcp_count and aws_count > 0:
                    synced_tables.append((table_name, gcp_count))
                else:
                    synced_tables.append((table_name, gcp_count))
            elif result is False:
                # Transfer failed or mismatch detected
                aws_count, gcp_count = get_row_counts(table_name)
                if gcp_count != aws_count:
                    mismatch_tables.append((table_name, aws_count, gcp_count))
                else:
                    failed_tables.append(table_name)
            
        except Exception as e:
            print(f"  ❌ Exception for {table_name}: {e}")
            failed_tables.append(table_name)
            continue
    
    # Print summary for this phase
    print(f"\n📊 Data Transfer Summary:")
    print(f"  • Successfully synced: {len(synced_tables)}")
    print(f"  • Mismatched counts: {len(mismatch_tables)}")
    print(f"  • Failed: {len(failed_tables)}")
    
    if mismatch_tables:
        print(f"\n⚠️ Tables with mismatched row counts:")
        for table, aws_c, gcp_c in mismatch_tables[:10]:
            print(f"  - {table}: AWS={aws_c}, GCP={gcp_c}")
        if len(mismatch_tables) > 10:
            print(f"  ... and {len(mismatch_tables) - 10} more")
    
    if failed_tables:
        print(f"\n❌ Tables that failed to transfer:")
        for table in failed_tables[:10]:
            print(f"  - {table}")
        if len(failed_tables) > 10:
            print(f"  ... and {len(failed_tables) - 10} more")
    
    print("\n" + "="*60)
    print("🔗 PHASE 4: CREATING FOREIGN KEYS")
    print("="*60 + "\n")
    
    # Step 4: Create foreign keys (after all tables and data exist)
    for table_name in tables:
        schema = table_schemas[table_name]
        if schema['foreign_keys']:
            print(f"🔗 Adding foreign keys for: {table_name}")
            create_foreign_keys(table_name, schema)
            try:
                gcp_conn.commit()
            except:
                gcp_conn.rollback()
    
    print("\n" + "="*60)
    print("🎉 MIGRATION COMPLETED!")
    print("="*60 + "\n")
    
    # Summary statistics
    total_tables = len(tables)
    synced_count = len(synced_tables) if 'synced_tables' in locals() else 0
    mismatch_count = len(mismatch_tables) if 'mismatch_tables' in locals() else 0
    failed_count = len(failed_tables) if 'failed_tables' in locals() else 0
    
    print(f"📊 Final Migration Summary:")
    print(f"  • Total tables: {total_tables}")
    print(f"  • ✅ Successfully synced: {synced_count}")
    print(f"  • ⚠️  Mismatched counts: {mismatch_count}")
    print(f"  • ❌ Failed: {failed_count}")
    
    # Calculate total rows transferred
    total_rows_synced = sum([count for _, count in synced_tables]) if synced_tables else 0
    print(f"  • 📦 Total rows synced: {total_rows_synced:,}")
    
    if mismatch_tables:
        print(f"\n⚠️ ATTENTION: Tables with row count mismatches:")
        for table, aws_c, gcp_c in mismatch_tables:
            print(f"  - {table}: AWS has {aws_c} rows, GCP has {gcp_c} rows")
        print("\n  Action needed: Review these tables manually")
    
    if failed_tables:
        print(f"\n❌ Tables that failed to transfer:")
        for table in failed_tables:
            print(f"  - {table}")
        print("\n  Action needed: Retry these tables manually or check error logs")
    
    if synced_count == total_tables:
        print("\n🎊 Perfect! All tables are synced successfully!")
        print("   GCP database now matches AWS database completely.")


# ----------------------------------------
# RUN MIGRATION
# ----------------------------------------
try:
    main()
except KeyboardInterrupt:
    print("\n\n⚠️ Migration interrupted by user")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ Migration failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
finally:
    # Close connections
    try:
        if aws_cur and not aws_cur.closed:
            aws_cur.close()
        if gcp_cur and not gcp_cur.closed:
            gcp_cur.close()
        if aws_conn and not aws_conn.closed:
            aws_conn.close()
        if gcp_conn and not gcp_conn.closed:
            gcp_conn.close()
        print("🔌 Database connections closed.")
    except:
        pass