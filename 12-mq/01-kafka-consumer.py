# Probably the best tutorial is this one: https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

from kafka import KafkaConsumer

consumer = KafkaConsumer('my_favorite_topic')
for message in consumer:
  print(message)

# For extra consumer features @see https://kafka-python.readthedocs.io/en/master/
