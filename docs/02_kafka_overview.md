Voici le fichier `docs/kafka-overview.md` complet, détaillé et structuré, prêt à être copié-collé :

```markdown
# Apache Kafka Overview

## 1. What is Apache Kafka?

Apache Kafka is a distributed event streaming platform that allows you to build real-time data pipelines and streaming applications. It acts as a high-throughput, fault-tolerant, scalable messaging system designed to handle large volumes of data with low latency.

### Simple Explanation

Imagine a big pipe through which messages flow continuously. Producers push messages into this pipe, and consumers pull messages out when they want to. Kafka organizes these messages in topics, which are like labeled channels inside the pipe.

---

## 2. Kafka Core Components

| Component    | Role                                               | Simple Analogy                     |
|--------------|---------------------------------------------------|----------------------------------|
| **Topic**    | Logical channel to organize messages by category | Different TV channels             |
| **Partition**| Subdivision of a topic for parallelism            | Multiple lanes on a highway       |
| **Producer** | Sends messages to a Kafka topic                    | Someone broadcasting a TV show   |
| **Consumer** | Reads messages from a Kafka topic                  | A viewer watching the TV show     |
| **Broker**   | Kafka server that stores and manages messages      | TV station infrastructure         |
| **Offset**   | Position of a message in a partition                | Episode number in a TV series     |

---

## 3. How Kafka Stores Messages

- Messages are appended to partitions in a strict order (append-only log).  
- Each message is assigned an **offset**, a unique number indicating its position in the partition.  
- Consumers read messages in order from their last committed offset, allowing replay of messages if needed.

---

## 4. Producers and Consumers

- **Producers** write data continuously to Kafka topics. They decide which partition to send a message to (using keys or round-robin).  
- **Consumers** subscribe to topics, reading messages starting at a specific offset. They can be grouped in **consumer groups** to distribute the load.

---

## 5. Why Not Use a Traditional Database?

| Aspect              | Kafka                                       | Traditional Database                     |
|---------------------|---------------------------------------------|-----------------------------------------|
| Data Access         | Append-only log, optimized for streaming    | Read/Write optimized, random access     |
| Latency            | Milliseconds, real-time streaming            | Typically slower for streaming scenarios|
| Scalability         | Horizontal scaling via partitions            | Scaling can be complex                   |
| Message Durability  | Configurable retention with replication      | Persistent storage, often ACID-compliant|
| Use Case            | Stream processing, event sourcing             | Transactional data, OLTP                 |

Kafka is designed for streaming and event-driven architectures, complementing databases rather than replacing them.

---

## 6. Important Kafka Features

### 6.1 Consumer Groups

- Multiple consumers can form a group. Kafka ensures each partition is consumed by only one consumer in the group, enabling parallel processing.

### 6.2 Offset Management

- Consumers track their progress by committing offsets. This allows consumers to resume reading after failures or restarts without data loss or duplication.

### 6.3 Message Retention

- Kafka retains messages for a configured time or size limit, even after consumption. This allows late consumers to catch up or replay messages.

---

## 7. Common Kafka Use Cases

- Real-time analytics and monitoring  
- Event sourcing and CQRS patterns  
- Log aggregation and processing  
- Stream processing pipelines  

---

## 8. Summary

Kafka is a powerful tool to build scalable, fault-tolerant streaming data pipelines. It enables decoupling of producers and consumers, allowing asynchronous, distributed processing of data streams.

---

## 9. Exercises & Thought Questions

- How would you design a consumer group for a high-throughput topic?  
- What are the implications of partition count on scalability and ordering?  
- How does Kafka handle fault tolerance and replication?  
- How do you ensure exactly-once processing semantics?

---

## 10. Further Reading

- [Apache Kafka Official Documentation](https://kafka.apache.org/documentation/)  
- [Kafka: The Definitive Guide](https://www.oreilly.com/library/view/kafka-the-definitive/9781491936153/)  
- [Confluent Kafka Tutorials](https://developer.confluent.io/learn-kafka/)

---

