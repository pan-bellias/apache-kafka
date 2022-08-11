from kafka import KafkaConsumer
import env as e
import json, time

consumer = KafkaConsumer(
    e.topic_b,
    e.group,
    bootstrap_servers=[e.bootstrap_servers],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

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
            print("Sum is: " + sum)
    else:
        prev_ts = ts