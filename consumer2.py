from kafka import KafkaConsumer, TopicPartition
import env as e

# manually assign the partition list for the consumer
consumer = KafkaConsumer(bootstrap_servers=e.bootstrap_servers)
consumer.assign([TopicPartition('foobar', 2)])
msg = next(consumer)