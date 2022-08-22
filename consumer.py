from kafka import KafkaConsumer
import env as e
import json, time

consumer = KafkaConsumer(
    e.topic_b,
    #e.group,
    bootstrap_servers=[e.bootstrap_servers],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

ph = -1
prev_ts = 0
print("Outside for")
for c in consumer:
    value = c.value
    ts = time.time()
    print("Outside 1 if")
    if c.key==b'PH':
        ph = value
        print("Inside 1 if")
    else:
        T = value
        print("Inside 1 else")
    print("Outside 2 if")
    if prev_ts != 0:
        diff = ts-prev_ts
        prev_ts = ts
        print("Inside 2 if")
        if diff <= 2.5:
            print(f"Success!\nT={T} and ph={ph}\nsec={diff}")
            sum = ph + T
            print("Sum is: " + sum)
    else:
        prev_ts = ts
        print("Inside 2 else")
    print("Inside for")
print("At the end")
