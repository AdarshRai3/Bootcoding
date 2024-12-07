-- Stored Routine : It is set of sql statement and quries which can be stored can be call when required.

-- Stored Procedure: It is set of sql statement and procdure logic by which we can perform operations like update,delete,insert and select.

Create or replace procedure add_products(p_name varchar(100),p_price decimal(10,2))
Language plpgsql  as  
$$ Start 
insert into products(pname,price) values(p_name,p_price);
End; $$;

-- By making this procedre we can perform opretation like add without riting the whole insert query.

call add_products('Laptop',50000);

------------------------------------------------------------------
-- Functions in sql

Create or replace function product_price(p_name varchar(100))
Returns (product_name varchar(100),p_price decimal(10,2)) Language Plpgsql as $$ Begin 
select pname,price from products where pname = p_name;
End; $$;

Select * from product_price('Laptop');
-------------------------------------------------------------------
Windows Function : Window functios are the analytical functions that are used to perform calculations across a set of rows related to the current row;

Define by an over() clause;
-------------------------------------------------------------------
