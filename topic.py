from kafka.admin import KafkaAdminClient, NewTopic

def create_topic():
    """
    Run this script once before starting your producer or consumer scripts.

    Check the output: it should say "Topic 'sensor-data' created successfully"
    or print an error if it already exists.

    Then run your data generator (producer) Python script to send data into Kafka.
    """
    admin_client = KafkaAdminClient(
        bootstrap_servers="localhost:9092",
        client_id='test_admin'
    )

    topic_list = []
    topic_list.append(NewTopic(name="sensor-data", num_partitions=3, replication_factor=1))
    
    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print("Topic 'sensor-data' created successfully.")
    except Exception as e:
        print(f"Error creating topic: {e}")

if __name__ == "__main__":
    create_topic()
