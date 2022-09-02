import json
import time
from kafka import KafkaConsumer, KafkaProducer

# define kafka consumer
consumer = KafkaConsumer(
    'my-topic-b',
    bootstrap_servers=["kafka:9092", "kafka-headless:9092"],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# define kafka producer
producer = KafkaProducer(
    bootstrap_servers=["kafka:9092", "kafka-headless:9092"],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

counter=0
ph = -1
prev_ts = 0
for c in consumer:
    value = c.value
    ts = time.time()
    if c.key==b'PH':
        ph = value
    else:
        T = value
    if prev_ts != 0:
        diff = ts-prev_ts
        prev_ts = ts
        if diff <= 2.5:
            print(f"Success!\nT={T} and ph={ph}\nsec={diff}")
            sum = ph + T
            print("Sum is: " + str(sum))

            # Write to TimescaleDB
            counter += 1
            data = {
                "schema": {
                    "type": "struct",
                    "optional": True,
                    "version": 1,
                    "fields": [
                        
                        # {
                        #     "field": "temperature",
                        #     "type": "float32",
                        #     "optional": False,
                        # },
                        # {
                        #     "field": "ph",
                        #     "type": "float32",
                        #     "optional": False
                        # },
                        # {
                        #     "field": "sum",
                        #     "type": "float32",
                        #     "optional": False
                        # },
                        
                        {
                            "field": "number",
                            "type": "int32",
                            "optional": True
                        }
                    ],
                    "payload": {
                        #"temperature": T,
                        #"ph": ph,
                        #"sum": sum,
                        "number": int(counter)
                    }
                }
            }
            producer.send('test-connect-7', value=data)

    else:
        prev_ts = ts