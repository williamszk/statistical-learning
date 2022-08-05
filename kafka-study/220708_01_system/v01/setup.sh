
docker-compose up -d

docker-compose down


# For the commands below we need to be inside a container
docker exec -it v01_kafka-1_1 /bin/bash

# create a topic
kafka-topics --create --bootstrap-server localhost:19092 --replication-factor 2 --partitions 2 --topic mytopic 

# how to see topics that were already created
kafka-topics --list --bootstrap-server localhost:19092

# create a producer
kafka-console-producer --broker-list localhost:19092 --topic mytopic

# start a temporary cosumer using the terminal
kafka-console-consumer --bootstrap-server localhost:19092 --topic mytopic --from-beginning


