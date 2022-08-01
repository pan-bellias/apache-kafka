from kafka import KafkaProducer
from kafka.errors import KafkaError

import env as e
import numpy as np

T = np.random.gamma(shape=2.0, scale=2.0)
while not 2 < T < 40:
    T = np.random.gamma(shape=2.0, scale=2.0)

print(f"Temperature: {T} oC")

producer = KafkaProducer(bootstrap_servers=[e.bootstrap_servers])

future = producer.send(e.topic_a, T)
try:
    record_metadata = future.get(timeout=50)
except KafkaError:
    print(str(KafkaError))
    pass

print(f"Temperature with value {record_metadata.value} oC sent to script 2")

future = producer.send(e.topic_b, T)
try:
    record_metadata = future.get(timeout=50)
except KafkaError:
    print(str(KafkaError))
    pass

print(f"Temperature with value {record_metadata.value} oC sent to script 3")