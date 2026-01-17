consumer.poll(timeout_ms=1000, max_records=500)
process_batch(records)
consumer.commit()
