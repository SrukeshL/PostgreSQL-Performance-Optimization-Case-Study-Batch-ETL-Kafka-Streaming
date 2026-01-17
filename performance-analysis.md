### Root Cause ###
- I/O bound extraction
- CPU-bound Python aggregation
- Kafka partition under-utilization

### Fix Summary ###
- SQL pushdown
- Batching
- Parallelism
