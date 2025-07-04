from confluent_kafka import Producer
import json
import random
import time

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(conf)

topic = 'sensor-data'

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"Record delivered to {msg.topic()} partition [{msg.partition()}] at offset {msg.offset()}")

def generate_sensor_data():
    # Simulate sensor data as a JSON dict
    return {
        "sensor_id": random.randint(1, 5),
        "timestamp": int(time.time()),
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 60.0), 2)
    }

if __name__ == "__main__":
    print("Starting data generator...")
    try:
        while True:
            data = generate_sensor_data()
            payload = json.dumps(data)
            # Produce to Kafka asynchronously
            producer.produce(topic=topic, value=payload, callback=delivery_report)
            producer.poll(0)  # serve delivery reports (non-blocking)
            time.sleep(1)  # produce one message per second
    except KeyboardInterrupt:
        print("Stopping data generator...")
    finally:
        producer.flush()
