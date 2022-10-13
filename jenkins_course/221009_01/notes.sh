
mkdir jenkins_home

touch docker-compose.yaml

docker-compose up -d

ca325456451c405aaff0104a5f6f08c2

william
1234
William Suzuki

# create a script outside the container
# then we copy it inside of the container

chmod +x script.sh

./script.sh William Suzuki 

# we could use volumes to share files between the host and the container

docker cp ./script.sh jenkins:/tmp/script.sh

docker exec -it jenkins /bin/bash

# video watching
# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12925870#overview

# 2022-10-11 next video:
# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12925952#overview