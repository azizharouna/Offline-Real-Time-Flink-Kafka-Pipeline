from kafka import KafkaAdminClient

def list_topics():
    admin_client = KafkaAdminClient(
        bootstrap_servers="localhost:9092",
        client_id='test_admin'
    )

    topics = admin_client.list_topics()
    print("Available topics:", topics)

if __name__ == "__main__":
    list_topics()
