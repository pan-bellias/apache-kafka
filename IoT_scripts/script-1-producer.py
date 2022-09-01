import time

import numpy, json
from kafka import KafkaProducer

# define kafka producer
producer = KafkaProducer(
    bootstrap_servers=["kafka:9092", "kafka-headless:9092"],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

while True:
    T = numpy.random.gamma(shape=2.0, scale=2.0)
    while T <= 2 or T >= 40:
        T = numpy.random.gamma(shape=2.0, scale=2.0)
    print(f"Generated temperature: {T}oC")

    producer.send('my-topic-a', key=b'Temperature', value=T)
    producer.send('my-topic-b', key=b'Temperature', value=T)
    producer.flush()
    time.sleep(5)