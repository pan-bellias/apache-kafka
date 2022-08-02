from kafka import KafkaConsumer, KafkaProducer
import env as e
import math, json
import threading

consumer = KafkaConsumer(
    e.topic_a,
    bootstrap_servers=[e.bootstrap_servers],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
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

    producer = KafkaProducer(
        bootstrap_servers=[e.bootstrap_servers],
        value_serializer=lambda m: json.dumps(m).encode('utf-8')
    )

    producer.send(e.topic_b, key=b'PH', value=ph)
    producer.flush()

send_ph()