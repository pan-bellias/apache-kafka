from kafka import KafkaProducer
from kafka.errors import KafkaError
import env as e
import logging as log
import msgpack, json

producer = KafkaProducer(
    bootstrap_servers=[e.bootstrap_servers],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
    )

producer.send(e.topic_a, 5.23)

# block until all async messages are sent
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5)
