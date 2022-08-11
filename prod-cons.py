from kafka import KafkaConsumer, KafkaProducer
import env as e
import math, json, time
# import threading

# print(e.topic_a)

producer = KafkaProducer(
    bootstrap_servers=e.bootstrap_servers,
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

consumer = KafkaConsumer(
    e.topic_a,
    e.group,
    bootstrap_servers=e.bootstrap_servers,
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

#def send_ph():
    # threading.Timer(7.0, send_ph).start()

i = 0
while True: #Two loops are needed. The while-loop makes the device sleep for 7 seconds and the for-loop picks up every message.
    print('rand')
    i += 1 
    if i != 1: #The first message from IoT1 must arrive immediatly, otherwise this device will sleep for 7 sec and ignore the first message that was written in the buffer.
        time.sleep(7)

    for message in consumer:
        T = message.value
        print(T)
        #break

        if T > 4.0:
            m = 6.4
            d = 0.15
            ph = 1/(math.sqrt(2*math.pi)*d)*math.exp(-(T-m)**2/(2*d**2))

            print(f"PH = {ph}")
            if ph < 0: print("Warning! PH is negative number!")
            elif ph > 14: print("Warning! PH is greater than 14!")
            else: print("Successful PH Calculation")

            producer.send(e.topic_b, key=b'PH', value=ph)
            producer.flush()
        
        break

#send_ph()