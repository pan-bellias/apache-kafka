from kafka import KafkaConsumer
import env as e

consumer = KafkaConsumer(e.topic_b, group_id=e.group, bootstrap_servers=[e.bootstrap_servers])
for message in consumer:
    print(f"{message} received")
