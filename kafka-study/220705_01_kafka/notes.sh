

# https://www.youtube.com/watch?v=SqVfCyfCJqw&ab_channel=Amigoscode


# Let's use a container that we already have to install Kafka related study 

docker start interesting_villani

# https://kafka.apache.org/quickstart#quickstart_startserver
# we download kafka and pass it to the container

# docker cp foo.txt container_id:/foo.txt
docker cp ~/Downloads/kafka_2.13-3.2.0 interesting_villani:/root/Kafka-Study/

docker exec -it interesting_villani /bin/bash 

cd kafka_2.13-3.2.0

ls

tmux 
apt update
apt upgrade -y
apt install tmux

tmux

# We need to install Java
# https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-20-04
java -version
apt install default-jre


# Run the following commands in order to start all services in the correct order:
# Start the ZooKeeper service
# Note: Soon, ZooKeeper will no longer be required by Apache Kafka.
bin/zookeeper-server-start.sh config/zookeeper.properties


# Open another terminal session and run:
# Start the Kafka broker service
bin/kafka-server-start.sh config/server.properties

# With this we have the Zookeeper and Kafka Broker Running


# The rest of the tutorial uses Spring Boot
# Maybe I should take a look at a tutorial of Kafka with Python
# We stoped at:

# https://youtu.be/SqVfCyfCJqw?t=922
