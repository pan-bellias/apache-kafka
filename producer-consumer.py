from kafka import KafkaConsumer
import env as e
import json, time

consumer = KafkaConsumer(
    e.topic_b,
    bootstrap_servers=[e.bootstrap_servers],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

i=1
prev_ts = 0
for c in consumer:
    value = c.value
    ts = time.time()
    if i%2==0:
        print("PH: ", value)
        ph = value
    else:
        print("Temperature: ", value)
        T = value
    if prev_ts != 0:
        diff = ts-prev_ts
        prev_ts = ts
        if diff <= 2.5:
            print(f"Success!\nT={T} and ph={ph}\nsec={diff}")
        else:
            print("Wrong period!")
    else:
        prev_ts = ts
    i+=1