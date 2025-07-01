# Kafka Internals: How Kafka Stores and Distributes Data

## 1. Kafka Storage Model

Kafka stores messages in **logs** — an ordered, immutable sequence of records.

- Each **topic** is split into one or more **partitions**.
- Each partition is a **commit log** stored on disk.
- Messages are **appended** to the end of the partition log.
- Kafka retains messages for a configurable retention period or until disk space runs out.

### Simplified analogy

Imagine a notebook where you only write new entries at the bottom, never erasing or rewriting.

---

## 2. How Partitions are Stored

- Each partition is assigned to a single **broker** that acts as the partition leader.
- The leader handles all reads and writes for that partition.
- Other brokers keep replicas for fault tolerance (called **followers**).
- If the leader fails, one of the followers is elected as the new leader.

---

## 3. Message Ordering

- Kafka guarantees that messages within a **single partition** are strictly ordered.
- Across partitions, there is no global ordering.

---

## 4. Message Offsets

- Every message has a unique **offset** within its partition.
- Offsets increase monotonically.
- Consumers use offsets to track their position in the log.

---

## 5. How Kafka Achieves Scalability

- By partitioning topics, Kafka distributes data across multiple brokers.
- Multiple consumers can read different partitions in parallel.
- Producers can write to multiple partitions concurrently.

---

## 6. Data Durability and Replication

- Partitions are **replicated** across multiple brokers for fault tolerance.
- The number of replicas is configurable per topic.
- Kafka uses a **leader-follower** replication model.
- A message is considered committed once it is written to the leader and replicated to followers.

---

## 7. Consumer Offset Management

- Consumers keep track of the last processed offset.
- Offsets can be stored in Kafka itself or externally.
- Allows consumers to restart and continue processing without data loss or duplication.

---

## 8. What Happens on Broker Failure?

- The followers detect leader failure through heartbeats.
- A new leader is elected from the in-sync replicas (ISR).
- This ensures high availability and fault tolerance.

---

## 9. Simplified Flow Summary

1. Producer sends a message to a topic partition leader.
2. Leader appends the message to its log.
3. Leader replicates the message to follower brokers.
4. Consumers read messages from the leader.
5. Consumers commit their offsets to track progress.

---

## 10. Questions for Reflection

- How does Kafka ensure consistency during leader failover?  
- What trade-offs exist between replication factor and performance?  
- How can consumers efficiently commit offsets without slowing down processing?  
- How does retention policy affect storage management?

---

## 11. Additional Resources

- Kafka Architecture Deep Dive: https://www.confluent.io/blog/kafka-fastest-messaging-system/  
- Kafka Replication Explained: https://kafka.apache.org/documentation/#replication  
- Managing Kafka Offsets: https://www.confluent.io/blog/consumer-offsets-in-kafka/

---
