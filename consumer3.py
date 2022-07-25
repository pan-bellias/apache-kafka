from kafka import KafkaConsumer
import msgpack
import env as e

# Deserialize msgpack-encoded values
consumer = KafkaConsumer(e.topic, value_deserializer=msgpack.loads)
consumer.subscribe(['msgpackfoo'])
for msg in consumer:
    assert isinstance(msg.value, dict)