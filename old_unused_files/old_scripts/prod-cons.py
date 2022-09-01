from kafka import KafkaConsumer, KafkaProducer
from os.path import dirname, join
import math, json
import threading
from dotenv import load_dotenv
import os
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
kafka_server=os.environ.get("BOOTSTRAP_SERVER")
topic_a = os.environ.get("TOPIC_A")

consumer = KafkaConsumer(
    topic_a,
#    e.group,
    bootstrap_servers=[kafka_server],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=[kafka_server],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

def send_ph():
    threading.Timer(7.0, send_ph).start()
    for message in consumer:
        T = message.value
        break

    if T > 4:
        pass
    m = 6.4
    d = 0.15
    ph = 1/(math.sqrt(2*math.pi)*d)*math.exp(-(T-m)**2/(2*d**2))

    print(f"PH = {ph}")
    if ph < 0: print("Warning! PH is negative number!")
    elif ph > 14: print("Warning! PH is greater than 14!")
    else: print("Successful PH Calculation")

    producer.send(e.topic_b, key=b'PH', value=ph)
    producer.flush()
    #sleep(7)

send_ph()

#i=0
#while i==0:
#    send_ph()
#    sleep(7)