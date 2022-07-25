from kafka import KafkaProducer
import env as e
import json

producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'), bootstrap_servers=e.bootstrap_servers)
producer.send(e.topic, {'foo': 'bar'})
