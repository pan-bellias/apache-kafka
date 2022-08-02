from kafka import KafkaProducer

import env as e
import numpy as np
import msgpack

T = np.random.gamma(shape=2.0, scale=2.0)
while not 2 < T < 40:
    T = np.random.gamma(shape=2.0, scale=2.0)

print(f"Temperature: {T} oC")

producer = KafkaProducer(bootstrap_servers=[e.bootstrap_servers], value_serializer=msgpack.dumps)

producer.send(e.topic_a, {'temperature': T})

producer.send(e.topic_b, {'temperature': T})