# https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05


# move the Kafka kernel closer to the study directory

cp -rp ~/Kafka-Study/kafka_2.13-3.2.0 ~/statistical-learning/kafka-study/

tmux

# Start tmux inside the kafka directory
# use ctrl+B " to divide horizontal panes
# or ctrl+B % to divide vertical panes


# We will need to use 3 panes in tmux

# Starting Zookeeper
# Kafka relies on Zookeeper, in order to make it run we will have to run Zookeeper 
# first.
bin/zookeeper-server-start.sh config/zookeeper.properties

# In another pane:
# Starting Kafka Server
# Next, we have to start Kafka broker server:
bin/kafka-server-start.sh config/server.properties


# Create Topics
# Messages are published in topics. Use this command to create a new topic.

# this will give an error:
# Exception in thread "main" joptsimple.UnrecognizedOptionException: zookeeper is 
# not a recognized option
# bin/kafka-topics.sh \
#     --create --zookeeper localhost:2181 \
#     --replication-factor 1 \
#     --partitions 1 \
#     --topic test

# https://stackoverflow.com/a/69550447/15875971
bin/kafka-topics.sh \
    --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic test

# we need to exclude Zookeeper and use bootstrap-server 

# This command will create a new topic
# called test

# Error while executing topic command : Timed out waiting for a node assignment. Call: createTopics
# 9092
# this is the correct port

# Now it works
# Created topic test.

# You can also list all available topics by running the following command.

bin/kafka-topics.sh --list --bootstrap-server localhost:9092
# root@2becc6d8ccd6:~/statistical-learning/kafka-study/kafka_2.13-3.2.0# bin/kafka-topics.sh --list --bootstrap-server localhost:9092
# test

# Sending Messages
# Next, we have to send messages, producers are used for that purpose. 
# Let’s initiate a producer.
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

# associate this with Wesley Willians tutorial about Kafka
# 

# We can write messages as this is the terminal of the producer
# Consuming Messages
bin/kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic test --from-beginning


# Install Kafka-Python
pip3 install kafka-python

# notes based on:
# https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05

# We are inside: ~/statistical-learning/kafka-study/kafka_2.13-3.2.0
# take a look inside of config/server.properties
vim config/server.properties

# find: advertised.listeners
PLAINTEXT://localhost:9092











