from kafka import KafkaConsumer
import env as e
import json, msgpack

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(e.topic_a,
                         e.group,
                         bootstrap_servers=[e.bootstrap_servers],
                        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

# consume earliest available messages, don't commit offsets
KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# consume json messages
KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))

# consume msgpack
KafkaConsumer(value_deserializer=msgpack.unpackb)

# StopIteration if no message after 1sec
KafkaConsumer(consumer_timeout_ms=1000)

# Subscribe to a regex topic pattern
consumer = KafkaConsumer()
consumer.subscribe(pattern='^awesome.*')

# Use multiple consumers in parallel w/ 0.9 kafka brokers
# typically you would run each on a different server / process / CPU
consumer1 = KafkaConsumer(e.topic_a,
                         e.group,
                         bootstrap_servers=[e.bootstrap_servers])
consumer2 = KafkaConsumer(e.topic_a,
                         e.group,
                         bootstrap_servers=[e.bootstrap_servers])