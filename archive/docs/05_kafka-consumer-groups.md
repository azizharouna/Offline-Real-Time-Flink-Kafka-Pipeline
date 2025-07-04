# Kafka Consumer Groups and Offset Management

## 1. What is a Consumer Group?

- A **consumer group** is a set of consumers that work together to consume messages from a topic.
- Each partition in the topic is consumed by **only one consumer** within the group.
- This allows for **parallel processing** and load balancing.

### Simplified analogy

Imagine a team of workers (consumers) picking apples from different trees (partitions). Each worker picks apples only from their assigned tree.

---

## 2. Benefits of Consumer Groups

- **Scalability**: Adding more consumers allows processing more partitions in parallel.
- **Fault tolerance**: If one consumer fails, another can take over its partitions.
- **Exactly-once processing** (when combined with offset commit management).

---

## 3. How Offsets Work in Consumer Groups

- Each consumer keeps track of the last **offset** it has processed in each partition.
- Offsets can be committed:
  - **Automatically** (periodically by Kafka client)
  - **Manually** (after processing the message)
- Committed offsets are stored in a special Kafka topic (`__consumer_offsets`).

---

## 4. Rebalancing in Consumer Groups

- When a consumer joins or leaves, Kafka **rebalances** partition assignments.
- During rebalance, consumers stop processing briefly to redistribute partitions.
- Proper rebalance handling is important to avoid duplicate processing or data loss.

---

## 5. Offset Reset Strategies

If a consumer starts and no committed offset is found, or the offset is invalid:

- **earliest**: start consuming from the earliest message in the partition.
- **latest**: start from the latest message (new messages).
- **none**: throw an error if no offset found.

---

## 6. Consumer Group Coordination

- Kafka uses a **group coordinator** broker to manage group membership.
- It keeps track of which consumer owns which partitions.
- The coordinator handles rebalances and offset commits.

---

## 7. Exactly-once vs At-least-once Processing

- Kafka guarantees **at-least-once** delivery by default.
- To achieve **exactly-once**, applications must carefully commit offsets **after** processing messages.
- Apache Flink integrates with Kafka to manage this more easily.

---

## 8. Questions for Reflection

- How does rebalancing affect message processing latency?  
- What are the pros and cons of auto-commit vs manual commit?  
- How does Flink integrate with Kafka’s offset management?  
- What happens if a consumer crashes before committing its offset?

---

## 9. Additional Resources

- Kafka Consumer Groups: https://kafka.apache.org/documentation/#consumerconfigs  
- Offset Management Guide: https://www.confluent.io/blog/kafka-fastest-messaging-system/#offsets  
- Exactly-once Processing with Kafka and Flink: https://ci.apache.org/projects/flink/flink-docs-stable/dev/connectors/kafka.html#exactly-once

---
