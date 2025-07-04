from kafka import KafkaConsumer
import json

def consume_data():
    consumer = KafkaConsumer(
        'sensor-data',                 # topic name
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',  # start reading from the earliest message
        group_id='sensor-group',       # consumer group id
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    print("Starting consumer...")

    try:
        for message in consumer:
            print(f"Received message from partition {message.partition} at offset {message.offset}: {message.value}")
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_data()
