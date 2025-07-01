from kafka import KafkaConsumer
import json

def run_consumer():
    consumer = KafkaConsumer(
        'sensor-data',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        group_id='sensor-processor-group'
    )

    high_temp_counts = {}
    message_count = 0
    batch_size = 10  # how often to print summary

    print("Starting consumer...")

    for message in consumer:
        data = message.value

        sensor_id = data['sensor_id']
        temperature = data['temperature']

        # Filter: Only consider temperature > 25°C
        if temperature > 25:
            high_temp_counts[sensor_id] = high_temp_counts.get(sensor_id, 0) + 1
            print(f"High temperature alert! Sensor {sensor_id} reported {temperature}°C")

        message_count += 1

        # Every batch_size messages, print summary and reset counts
        if message_count % batch_size == 0:
            print("---- Aggregation Summary ----")
            for sid, count in high_temp_counts.items():
                print(f"Sensor {sid}: {count} high temp alerts in last {batch_size} messages")
            print("----------------------------")
            high_temp_counts.clear()

if __name__ == "__main__":
    run_consumer()
