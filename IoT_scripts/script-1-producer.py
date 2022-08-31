import os
import time
from os.path import dirname, join

import numpy, json
from dotenv import load_dotenv
from kafka import KafkaProducer

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
# define kafka producer
producer = KafkaProducer(
    bootstrap_servers=[os.environ.get("BOOTSTRAP_SERVER")],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

while True:
    T = numpy.random.gamma(shape=2.0, scale=2.0)
    while T <= 2 or T >= 40:
        T = numpy.random.gamma(shape=2.0, scale=2.0)
    print(f"Generated temperature: {T}oC")

    producer.send(os.environ.get("TOPIC_A"), key=b'Temperature', value=T)
    producer.send(os.environ.get("TOPIC_B"), key=b'Temperature', value=T)
    producer.flush()
    time.sleep(5)