from ensurepip import bootstrap
import os
import time
from os.path import dirname, join

import numpy, json
from dotenv import load_dotenv
from kafka import KafkaConsumer, KafkaProducer

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
# define kafka consumer
consumer = KafkaConsumer(
    os.environ.get("TOPIC_A"),
    bootstrap_servers=[os.environ.get("BOOTSTRAP_SERVER")],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    t = message.value
    print(t)
    break