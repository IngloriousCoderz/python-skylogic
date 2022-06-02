from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:1234')
for _ in range(100):
  producer.send('foobar', b'some_message_bytes')

# For extra producer features @see https://kafka-python.readthedocs.io/en/master/#kafkaproducer