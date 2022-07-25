from kafka import KafkaProducer
import env as e

producer = KafkaProducer(bootstrap_servers=e.bootstrap_servers)
for _ in range(100):
    producer.send(e.topic, value=b'some_message_bytes')