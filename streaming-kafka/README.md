## Kafka Streaming Pipeline

### Original Issue
- Single consumer processing all partitions
- No batching
- At-least-once semantics causing duplicates
- Consumer lag increasing under burst traffic

### Improvements
- Partition-aware consumers
- Batched polling
- Manual offset commits
- Backpressure handling
