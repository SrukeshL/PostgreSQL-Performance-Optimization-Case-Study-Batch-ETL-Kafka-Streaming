producer.send(
    topic,
    key=str(order_id).encode(),
    value=payload
)
