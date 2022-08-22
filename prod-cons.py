from kafka import KafkaConsumer, KafkaProducer
import env as e
import math, json
import threading
from time import sleep

print(e.topic_a)

consumer = KafkaConsumer(
    e.topic_a,
#    e.group,
    bootstrap_servers=[e.bootstrap_servers],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=[e.bootstrap_servers],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

def send_ph():
    #threading.Timer(7.0, send_ph).start()
#i=0
#while i==0:
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

#send_ph()

i=0
while i==0:
    send_ph()
    sleep(7)
