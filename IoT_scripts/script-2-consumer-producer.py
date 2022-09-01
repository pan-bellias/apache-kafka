import json, math
import time
from kafka import KafkaConsumer, KafkaProducer

# define kafka consumer
consumer = KafkaConsumer(
    'my-topic-a',
    bootstrap_servers=["kafka:9092", "kafka-headless:9092"],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# define kafka producer
producer = KafkaProducer(
    bootstrap_servers=["kafka:9092", "kafka-headless:9092"],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

while True:
    for message in consumer:
        if message.key == b"Temperature":
            temperature = float(message.value)
            print("Temperature taken: " + str(temperature))
        break

    if not temperature or temperature > 4.0:
        continue

    m = 6.4
    d = 0.15
    ph = 1/(math.sqrt(2*math.pi)*d)*math.exp(-(temperature-m)**2/(2*d**2))

    print(f"PH calculated= {ph}")
    if ph < 0: print("Warning! PH is negative number!")
    elif ph > 14: print("Warning! PH is greater than 14!")
    else: print("Successful PH Calculation")

    producer.send('my-topic-b', key=b'PH', value=ph)
    producer.flush()

    time.sleep(7)