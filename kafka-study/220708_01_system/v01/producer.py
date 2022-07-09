# https://github.com/confluentinc/confluent-kafka-python

# Take a look at:
# https://github.com/confluentinc/examples/tree/master/clients/cloud/python 
from confluent_kafka import Producer

# what goes inside the mybroker1?
# p = Producer({'bootstrap.servers': 'mybroker1,mybroker2'})
p = Producer({'bootstrap.servers': 'mybroker1'})





