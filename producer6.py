from kafka import KafkaProducer
import env as e

producer = KafkaProducer(compression_type='gzip', bootstrap_servers=e.bootstrap_servers)
for i in range(1000):
    producer.send(e.topic, b'msg %d' % i)