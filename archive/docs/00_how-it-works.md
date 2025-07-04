## Data Generator (Producer) — `data_generator.py`

This Python script simulates sensor data and sends it as messages to the Kafka topic `sensor-data` at a regular interval (1 message per second).

### How it works

- **Simulates sensor readings:**  
  Each message contains a sensor ID, temperature, humidity, and a timestamp. The values are randomly generated to mimic real IoT sensors.

- **Kafka Producer:**  
  The script creates a Kafka producer connected to the local Kafka broker at `localhost:9092`. It serializes the sensor data into JSON format before sending.

- **Continuous streaming:**  
  In an infinite loop, the script generates new sensor data every second and sends it to Kafka.

- **Graceful shutdown:**  
  When interrupted (Ctrl+C), the script cleanly closes the Kafka connection.

### Analogy

Think of Kafka as a post office and this script as the mail carrier who writes and drops one letter (message) every second into the post office (Kafka topic). These messages can then be picked up by consumers for processing.

### Why is this important?

- Shows how real-time data ingestion works with Kafka.  
- Provides a simple example of a Kafka producer in Python.  
- Sets up the data stream that downstream components (like Apache Flink) will consume and process.

---

### Running the data generator

```bash
python data_generator.py




## Flink Job (Consumer & Processor) — `flink_job.py`

This Python script uses **Apache Flink (PyFlink)** to consume streaming data from the Kafka topic `sensor-data`, process it in real-time, and save the processed results locally.

### How it works

- **Kafka Consumer:**  
  Connects to the Kafka topic `sensor-data` to continuously read sensor messages as they arrive.

- **Stream Processing:**  
  Processes data on-the-fly using Flink’s powerful stream processing capabilities. Example operations might include filtering, aggregation, or windowing (grouping data over time intervals).

- **Output to local storage:**  
  Writes processed results to local files (e.g., CSV or JSON) for further analysis.

- **Fault tolerance and checkpointing:**  
  Flink supports checkpointing and state management to ensure exactly-once processing semantics and resilience in case of failure (depending on configuration).

### Analogy

Imagine Flink as a factory on a production line that continuously receives raw materials (sensor messages) and transforms them into finished goods (processed data) ready to be stored or analyzed.

### Why is this important?

- Demonstrates real-time stream processing with Apache Flink.  
- Shows how to integrate Flink with Kafka as a data source.  
- Provides the core logic for analyzing live data streams and producing actionable output.

---

### Running the Flink job

```bash
python flink_job.py
