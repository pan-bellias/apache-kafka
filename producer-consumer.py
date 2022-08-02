from kafka import KafkaConsumer
import env as e
import json

consumer = KafkaConsumer(
    e.topic_b,
    bootstrap_servers=[e.bootstrap_servers],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

i=1
for c in consumer:
    if i == 1:
        T = c.value
        print(T)
    if i == 2:
        ph = c.value
        print(ph)
        break
    i+=1

print(f"Success!\n T={T} and ph={ph}")