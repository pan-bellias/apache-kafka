from kafka import KafkaProducer

import env as e
import numpy as np
import json
import threading

producer = KafkaProducer(
    bootstrap_servers=[e.bootstrap_servers],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

def send_temperature():
    threading.Timer(5.0, send_temperature).start()
    T = np.random.gamma(shape=2.0, scale=2.0)
    while not 2 < T < 40:
        T = np.random.gamma(shape=2.0, scale=2.0)

    print(f"Temperature: {T} oC")

    producer.send(e.topic_a, T)
    producer.send(e.topic_b, T)
    producer.flush()

send_temperature()