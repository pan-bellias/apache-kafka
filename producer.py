from kafka import KafkaProducer

import env as e
import numpy as np
import json

T = np.random.gamma(shape=2.0, scale=2.0)
while not 2 < T < 40:
    T = np.random.gamma(shape=2.0, scale=2.0)

print(f"Temperature: {T} oC")

producer = KafkaProducer(
    bootstrap_servers=[e.bootstrap_servers],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

producer.send(e.topic_a, T)
producer.send(e.topic_b, T)
producer.flush()