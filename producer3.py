from kafka import KafkaProducer
import env as e

producer = KafkaProducer(bootstrap_servers=e.bootstrap_servers)
producer.send(e.topic, key=b'foo', value=b'bar')