from kafka import KafkaProducer
import env as e

producer = KafkaProducer(key_serializer=str.encode, bootstrap_servers=e.bootstrap_servers)
producer.send(e.topic, key='ping', value=b'1234')