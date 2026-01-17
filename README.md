# Performance Optimization Case Study: Batch ETL + Near-Real-Time Kafka Streaming ##

## Problem Statement ##
A hybrid data pipeline handling both batch ETL and real-time Kafka streaming
experienced severe performance degradation, data latency, and resource contention
under increasing data volume.

## Impact ##
- Batch ETL runtime increased from 35 mins → 3+ hours
- Kafka consumer lag exceeded SLA (30+ minutes)
- CPU & memory saturation on shared nodes
- Missed downstream reporting deadlines

## Solution Summary ##
- Optimized batch ETL execution (I/O, SQL, memory)
- Introdued partition-aware Kafka consumption
- Implemented backpressure and batching
- Added observability and alerting
- Reduced overall pipeline latency by **~70%**

## Tech Stack ##
- Python
- Kafka
- PostgreSQL / Cloud Data Warehouse
- Prometheus-style metrics
