from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types

import json
from collections import deque, defaultdict

# Define the temperature threshold
HIGH_TEMP_THRESHOLD = 25.0

# A simple stateful class to track recent high-temperature events
class AlertTracker:
    def __init__(self, max_size=10):
        self.recent_alerts = deque(maxlen=max_size)
        self.alert_counts = defaultdict(int)

    def add_alert(self, sensor_id):
        self.recent_alerts.append(sensor_id)
        self.recount()

    def recount(self):
        self.alert_counts = defaultdict(int)
        for sid in self.recent_alerts:
            self.alert_counts[sid] += 1

    def print_summary(self):
        print("---- Aggregation Summary ----")
        for sid, count in self.alert_counts.items():
            print(f"Sensor {sid}: {count} high temp alerts in last {len(self.recent_alerts)} messages")
        print("----------------------------")

# Parse incoming Kafka message
def parse_sensor_data(msg):
    try:
        data = json.loads(msg)
        return (data["sensor_id"], data["timestamp"], data["temperature"], data["humidity"])
    except Exception as e:
        print(f"Error parsing: {e}")
        return None

# Filter function to detect high temperature
def is_high_temperature(record):
    return record and record[2] >= HIGH_TEMP_THRESHOLD

# The main Flink job
def flink_job():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # Kafka source configuration
    kafka_consumer = FlinkKafkaConsumer(
        topics='sensor-data',
        deserialization_schema=SimpleStringSchema(),
        properties={
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'flink-group'
        }
    )

    stream = env.add_source(kafka_consumer)

    # Parse and convert each JSON string to a structured tuple
    parsed_stream = stream.map(parse_sensor_data, output_type=Types.TUPLE([Types.INT(), Types.LONG(), Types.FLOAT(), Types.FLOAT()]))

    # Filter high temperature events
    high_temp_stream = parsed_stream.filter(is_high_temperature)

    # Track and summarize alerts using custom Python logic
    alert_tracker = AlertTracker()

    def process_alert(record):
        sensor_id, ts, temp, humidity = record
        print(f"High temperature alert! Sensor {sensor_id} reported {temp}°C")
        alert_tracker.add_alert(sensor_id)
        if len(alert_tracker.recent_alerts) >= 10:
            alert_tracker.print_summary()

    high_temp_stream.map(process_alert, output_type=Types.VOID())

    env.execute("Sensor High Temperature Alert Job")

if __name__ == '__main__':
    flink_job()
