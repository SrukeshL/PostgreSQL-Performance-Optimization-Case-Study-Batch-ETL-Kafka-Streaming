# extract.py
import psycopg2

def extract_incremental(conn, last_updated):
    cursor = conn.cursor(name="etl_cursor")
    cursor.execute("""
        SELECT *
        FROM orders
        WHERE updated_at > %s
    """, (last_updated,))

    for batch in iter(lambda: cursor.fetchmany(5000), []):
        yield batch
