from kafka import KafkaProducer
import env as e

producer = KafkaProducer(e.topic, bootstrap_servers=e.bootstrap_servers)
future = producer.send(b'another_message')
result = future.get(timeout=60)
producer.flush()