
docker-compose up -d
# Pulling zookeeper-1 (confluentinc/cp-zookeeper:latest)...
# latest: Pulling from confluentinc/cp-zookeeper
# a9e23b64ace0: Pull complete
# 38b71301a1d9: Pull complete
# 51a890b0d424: Pull complete
# 08ad99821f58: Pull complete
# 6a7c13ed9f73: Pull complete
# cf35f0d13f7d: Pull complete
# e318c2c4af84: Pull complete
# 80e95edc5152: Pull complete
# cb8d0317eb61: Pull complete
# d6c446155168: Pull complete
# 7da07b608cf4: Pull complete
# Digest: sha256:31f5992546679a5c70bf10b2f1b6c9c5c4d8e5bb585a62e637a4b1b872709bbe
# Status: Downloaded newer image for confluentinc/cp-zookeeper:latest
# Pulling kafka-1 (confluentinc/cp-kafka:latest)...
# latest: Pulling from confluentinc/cp-kafka
# a9e23b64ace0: Already exists
# 38b71301a1d9: Already exists
# 51a890b0d424: Already exists
# 08ad99821f58: Already exists
# 6a7c13ed9f73: Already exists
# cf35f0d13f7d: Already exists
# e318c2c4af84: Already exists
# 80e95edc5152: Already exists
# cb8d0317eb61: Already exists
# 85297e61ac4d: Pull complete
# e2cba4a86a94: Pull complete
# Digest: sha256:5f3cdbebbd9efdb805a8af27f904b6ac5ac43a24084700009f8ec0a31ccd46a6
# Status: Downloaded newer image for confluentinc/cp-kafka:latest
# Creating 220704_01_zookeeper-1_1 ... done
# Creating 220704_01_zookeeper-3_1 ... done
# Creating 220704_01_zookeeper-2_1 ... done
# Creating 220704_01_kafka-3_1     ... done
# Creating 220704_01_kafka-1_1     ... done
# Creating 220704_01_kafka-2_1     ... done

docker ps
# CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS          PORTS     NAMES
# abfe5d07f2e3   confluentinc/cp-kafka:latest       "/etc/confluent/dock…"   19 minutes ago   Up 19 minutes             220704_01_kafka-2_1
# 2802d1a919e6   confluentinc/cp-kafka:latest       "/etc/confluent/dock…"   19 minutes ago   Up 19 minutes             220704_01_kafka-1_1
# c1d4dbed864c   confluentinc/cp-kafka:latest       "/etc/confluent/dock…"   19 minutes ago   Up 19 minutes             220704_01_kafka-3_1
# a00687f70ade   confluentinc/cp-zookeeper:latest   "/etc/confluent/dock…"   19 minutes ago   Up 19 minutes             220704_01_zookeeper-2_1
# ac752c763f4c   confluentinc/cp-zookeeper:latest   "/etc/confluent/dock…"   19 minutes ago   Up 19 minutes             220704_01_zookeeper-1_1
# 7406262f9eb1   confluentinc/cp-zookeeper:latest   "/etc/confluent/dock…"   19 minutes ago   Up 19 minutes             220704_01_zookeeper-3_1

# enter inside a container running kafka
docker exec -it 220704_01_kafka-2_1 /bin/bash

# create a topic
kafka-topics --create --bootstrap-server localhost:29092 --replication-factor 3 --partitions 3 --topic mytopic
# [appuser@william-ThinkPad-T450 ~]$ kafka-topics --create --bootstrap-server localhost:29092 --replication-factor 3 --partitions 3 --topic mytopic
# Created topic mytopic.

# how to see topics that were already created
kafka-topics --list --bootstrap-server localhost:29092

# send a message to a topic using the terminal instead of a program
kafka-console-producer --broker-list localhost:29092 --topic mytopic
# this open a command prompt to write a message

# in another terminal
docker exec -it 220704_01_kafka-2_1 /bin/bash
# this will act as the consumer
kafka-console-consumer --bootstrap-server localhost:29092 --topic mytopic

# on the producer terminal we write a message
hello full cycle
# this message will appear inside the consumer

# Kafka will not remove the already consumed messages
# we can access the old messages, RabbitMQ will remove old messages

# we can set the consumer to consumer from the beginning of the topic
kafka-console-consumer --bootstrap-server localhost:29092 --topic mytopic --from-beginning

# we can create many consumers
# we can create groups
# each consumer group will act as a parallel processor

# in two different terminals we can run this command
docker exec -it 220704_01_kafka-2_1 /bin/bash
kafka-console-consumer --bootstrap-server localhost:29092 --topic mytopic --from-beginning --group groupA

# from the producer we can write messages
# and those messages will go to each consumer depending on which 
# partition the message went
kafka-topics --describe --bootstrap-server localhost:29092 --topic mytopic
# Topic: mytopic  TopicId: zlmeaHCJS3OdCCeI4TpNpQ PartitionCount: 3       ReplicationFactor: 3    Configs: 
#         Topic: mytopic  Partition: 0    Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
#         Topic: mytopic  Partition: 1    Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
#         Topic: mytopic  Partition: 2    Leader: 3       Replicas: 3,1,2 Isr: 3,1,2


# for this command to work we need to have clients running
kafka-consumer-groups --group groupA --bootstrap-server localhost:29092 --describe
# GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                           HOST            CLIENT-ID
# groupA          mytopic         0          8               8               0               console-consumer-4a225ed7-4dc8-4cd7-879e-17e234ac07a2 /127.0.0.1      console-consumer
# groupA          mytopic         1          5               5               0               console-consumer-4a225ed7-4dc8-4cd7-879e-17e234ac07a2 /127.0.0.1      console-consumer
# groupA          mytopic         2          3               3               0               console-consumer-4b1cfb10-a202-46cc-b8a7-96bebb280c44 /127.0.0.1      console-consumer








# Terminate all containers
docker-compose down


