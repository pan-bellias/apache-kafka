from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
import env as e
import math

consumer = KafkaConsumer(e.topic_a, group_id=e.group, bootstrap_servers=[e.bootstrap_servers])
for T in consumer:
    print(f"{T} oC received")

if T > 4:
    ph = 3
else:
    m = 6.4
    d = 0.15
    ph = 1/(math.sqrt(2*math.pi)*d)*math.exp(-(T-m)**2/(2*d**2))

print(f"PH = {ph}")
if ph < 0: print("Warning! PH is negative number!")
if ph > 14: print("Warning! PH is greater than 14!")

producer = KafkaProducer(bootstrap_servers=[e.bootstrap_servers])

future = producer.send(e.topic_b, ph)
try:
    record_metadata = future.get(timeout=50)
except KafkaError:
    print(str(KafkaError))
    pass

print(f"PH with value {record_metadata.value} sent to script 3")