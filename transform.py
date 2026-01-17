def transform(records):
    return [
        {
            "order_id": r[0],
            "amount": float(r[3]),
            "region": r[5],
            "event_date": r[6].date()
        }
        for r in records
    ]
