def bulk_load(conn, rows):
    with conn.cursor() as cur:
        cur.executemany("""
            INSERT INTO fact_orders (order_id, amount, region, event_date)
            VALUES (%(order_id)s, %(amount)s, %(region)s, %(event_date)s)
        """, rows)
