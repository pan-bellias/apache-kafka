from kafka import KafkaConsumer
import env as e

# join a consumer group for dynamic partition assignment and offset commits
consumer = KafkaConsumer(e.topic, group_id=e.group)
for msg in consumer:
    print (msg)