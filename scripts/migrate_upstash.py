import os
import json
import requests
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
from upstash_redis import Redis

BATCH_SIZE = 300
THREADS = 6


#---------------------------------------------
#.env example values 

# SRC_REDIS_REST_URL=
# SRC_REDIS_REST_TOKEN=


# DST_REDIS_REST_URL=
# DST_REDIS_REST_TOKEN=

#---------------------------------------------
#Requirements:
# pip install upstash-redis requests python-dotenv


# -------------------------------
# Load clients
# -------------------------------
def get_clients():
    load_dotenv(".env.example")

    src = Redis(
        url=os.getenv("SRC_REDIS_REST_URL"),
        token=os.getenv("SRC_REDIS_REST_TOKEN")
    )

    # For destination, we need the raw REST endpoint
    dst_rest_url = os.getenv("DST_REDIS_REST_URL")
    dst_token = os.getenv("DST_REDIS_REST_TOKEN")

    return src, dst_rest_url, dst_token


# -------------------------------
# Build raw multi-command payload
# -------------------------------
def send_multi_exec(dst_url, dst_token, commands):
    """
    Commands = list of ["SET", "key", "value"] etc.
    Sends ALL commands via one HTTP request.
    """
    headers = {
        "Authorization": f"Bearer {dst_token}",
        "Content-Type": "application/json",
    }

    resp = requests.post(
        url=f"{dst_url}/multi-exec",
        headers=headers,
        data=json.dumps(commands),
        timeout=30
    )

    if resp.status_code != 200:
        print("🚨 Multi-exec failed:", resp.text)

    return resp.json()


# -------------------------------
# Process a batch with ONE network call
# -------------------------------
def migrate_batch(src, dst_url, dst_token, keys, batch_id):
    cmds = []

    for key in keys:
        t = src.type(key)
        ttl = src.pttl(key)

        # ---- STRING ----
        if t == "string":
            v = src.get(key)
            cmds.append(["SET", key, v])

        # ---- HASH ----
        elif t == "hash":
            h = src.hgetall(key)
            if h:
                flat = []
                for f, v in h.items():
                    flat.extend([f, v])
                cmds.append(["HSET", key] + flat)

        # ---- LIST ----
        elif t == "list":
            lst = src.lrange(key, 0, -1)
            if lst:
                cmds.append(["RPUSH", key] + lst)

        # ---- SET ----
        elif t == "set":
            s = src.smembers(key)
            if s:
                cmds.append(["SADD", key] + list(s))

        # ---- ZSET ----
        elif t == "zset":
            z = src.zrange(key, 0, -1, withscores=True)
            if z:
                flat = []
                for m, s in z:
                    flat.extend([float(s), m])
                cmds.append(["ZADD", key] + flat)

        # ---- JSON ----
        elif t in ("ReJSON-RL", "json"):
            v = src.json.get(key, "$")
            cmds.append(["JSON.SET", key, "$", json.dumps(v[0])])

        # ---- TTL ----
        if ttl and ttl > 0:
            cmds.append(["PEXPIRE", key, ttl])

    # ONE request for entire batch
    send_multi_exec(dst_url, dst_token, cmds)

    print(f"[THREAD] Batch {batch_id} done ({len(keys)} keys)")


# -------------------------------
# SCAN + multithread migrate
# -------------------------------
def migrate_all():
    src, dst_url, dst_token = get_clients()

    cursor = 0
    batches = []
    batch_id = 0

    print("Scanning keys...")

    while True:
        cursor, keys = src.scan(cursor, count=BATCH_SIZE)
        if keys:
            batches.append(keys)

        if cursor == 0:
            break

    print(f"Total batches: {len(batches)}")

    print(" Starting migration...")

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = []
        for keys in batches:
            batch_id += 1
            futures.append(
                executor.submit(migrate_batch, src, dst_url, dst_token, keys, batch_id)
            )

        for fut in as_completed(futures):
            fut.result()

    print("\ DONE — Full multi-threaded, multi-exec migration complete!")


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    migrate_all()


#---------------------------------------------
#.env example values 

# SRC_REDIS_REST_URL=
# SRC_REDIS_REST_TOKEN=


# DST_REDIS_REST_URL=
# DST_REDIS_REST_TOKEN=

#---------------------------------------------
#Requirements:
# pip install upstash-redis requests python-dotenv