
```markdown
# Real-Time Streaming Data Pipeline with Apache Flink & Kafka (No Cloud)

This project simulates a real-time data pipeline using **Apache Flink** and **Apache Kafka**, designed to run locally in **GitHub Codespaces** without requiring any cloud resources.

---

## 📌 Project Goals

- Simulate real-time data ingestion (e.g. IoT sensor stream)  
- Use **Apache Kafka** as the event streaming platform (Kinesis equivalent)  
- Use **Apache Flink (PyFlink)** to process streaming data  
- Store processed results locally (CSV or JSON)  
- (Optional) Analyze results with Pandas or DuckDB

---

## 🚀 What is Apache Kafka?

Apache Kafka is a distributed event streaming platform used to build real-time data pipelines and streaming applications. It allows applications to publish (produce) and subscribe to (consume) streams of records, similar to a messaging system but designed for high throughput and scalability.

### Key Concepts

| Term         | Description                                                   |
|--------------|---------------------------------------------------------------|
| **Topic**    | Logical channel or category for messages                       |
| **Partition**| A division of a topic to allow parallelism and scalability    |
| **Producer** | Application that sends messages to a Kafka topic              |
| **Consumer** | Application that reads messages from a Kafka topic            |
| **Broker**   | Kafka server that stores and manages messages                  |
| **Offset**   | Unique identifier of a message within a partition (position)  |

Kafka stores messages in partitions as immutable, ordered logs. Producers append messages, consumers read from a given offset, allowing replay and fault tolerance.

---

## ⚙️ Why Use Kafka Instead of a Traditional Database?

- **Scalability:** Partitions allow load distribution across brokers.  
- **Durability:** Messages are retained for configurable durations, even after consumption.  
- **Low Latency:** Designed for real-time streaming data with minimal delays.  
- **Fault Tolerance:** Replication ensures data survives broker failures.

Kafka is not meant to replace databases but to complement them in streaming architectures.

---

## 🏗 Architecture Overview

```

Producer ---> Kafka Topic (Partitions) ---> Broker(s) ---> Consumer(s)

````

- Producers write data continuously into topic partitions.  
- Brokers manage storage and replication.  
- Consumers read and process data independently, keeping track of offsets.

---

## 🔑 Additional Concepts

- **Consumer Groups:** Multiple consumers can share load by belonging to the same group; each partition is consumed by one consumer in the group.  
- **Offsets:** Consumers track their position in partitions via offsets, enabling message replay and fault recovery.  
- **Retention Policy:** Configurable duration Kafka retains messages before deletion.

---

## 🛠 Tech Stack

| Component      | Tool Used              |
| -------------- | ---------------------- |
| Data Streaming | Apache Kafka           |
| Processing     | Apache Flink (PyFlink) |
| Storage        | Local filesystem       |
| Analysis       | Pandas / DuckDB        |

---

## 🧪 Running the Pipeline

### 1. Start Kafka and Zookeeper

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
````

### 2. Create Kafka Topic

```bash
bin/kafka-topics.sh --create --topic sensor-data --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```

### 3. Run Data Generator (Producer)

```bash
python data_generator.py
```

### 4. Run Flink Job (Consumer & Processor)

```bash
python flink_job.py
```

---

## 📚 Glossary

* **Topic:** Channel where messages are published.
* **Partition:** Subdivision of a topic for scalability.
* **Producer:** Sends messages to Kafka.
* **Consumer:** Reads messages from Kafka.
* **Broker:** Kafka server node.
* **Offset:** Position of a message in a partition.

---

## 💡 Exercises & Ideas

* Create multiple partitions to distribute load across consumers.
* Implement consumer groups to enable parallel processing.
* Explore offset management to implement exactly-once processing semantics.

---

## 📬 Contact

Feel free to contribute or ask questions via GitHub Issues.

---

## ✅ Status

✔ Works 100% offline
✔ Fully runnable in GitHub Codespaces
✔ Mimics a real AWS Kinesis-Flink-S3 pipeline

---


