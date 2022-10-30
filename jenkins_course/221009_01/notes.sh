
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


# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12925952?start=15#overview

# this directory is a volume for the other container that we'll create
mkdir centos7
touch centos7/Dockerfile

docker pull centos

# create ssh keys
ssh-keygen -f my-remote-key

# we've updated the docker-compose file
# with this command we are going to just build the images
# declared inside this docker-compose file
docker-compose build

# this will read the docker-compose.yaml file and create what is left
docker-compose up -d

docker-compose ps

# enter into the jenkins container
docker exec -it jenkins bash

# [inside jenkins container]
# ssh into the remote-host container
ssh remote_user@remote_host
# we can use the name of the service defined in the docker-compose file
# because docker creates an internal DNS

# now we are inside the remote_host container

# go back to the host machine
# copy the private key of remote_host container into the jenkins container
docker cp ./centos7/my-remote-key jenkins:/tmp/my-remote-key

# we can enter into the jenkins container again
docker exec -it jenkins bash
# [inside the jenkins container]

# then we can ssh into the remote_host container
ssh -i /tmp/my-remote-key remote_user@remote_host
# in this way ssh will not ask for a password

# next video:
# https://www.udemy.com/course/jenkins-from-zero-to-hero/learn/lecture/12925972#overview

docker-compose start

# we could share keys in two manners:
# we could create a key pair in the client, then include the public key of
# the client inside the server's .ssh directory
docker exec -it remote-host bash
# [inside the remote-host container]
cd /home/remote_user/.ssh/
cat authorized_keys
exit

# experiment creating another key pair and using it to 
# use the jenkins container to ssh into the remote-host container
# inside the jenkins container generate keys
docker exec -it jenkins bash
# [inside the jenkins container]
ssh-keygen -f my-experiment-key
    # jenkins@9ad0f1d92378:/$ ssh-keygen -f my-experiment-key
    # Generating public/private rsa key pair.
    # Enter passphrase (empty for no passphrase): 
    # Enter same passphrase again: 
    # Saving key "my-experiment-key" failed: Permission denied
# The problem is that I'm not the root user
# maybe I should create the key in another directory

cd /tmp/
ssh-keygen -f my-experiment-key
# this one worked!
# I needed to change the directory to tmp
# this would work if tmp was owned by the jenkins user
    # drwxrwxrwt   1 root root 4096 Oct 17 13:59 tmp
# the tmp directoy belongs to the root
# idk then...
    # jenkins@9ad0f1d92378:/tmp$ ssh-keygen -f my-experiment-key
    # Generating public/private rsa key pair.
    # Enter passphrase (empty for no passphrase): 
    # Enter same passphrase again: 
    # Your identification has been saved in my-experiment-key
    # Your public key has been saved in my-experiment-key.pub
    # The key fingerprint is:
    # SHA256:Lt4wGUU3t7P7zJ7hVIilQllKrXW74+w7l7m4dYXBhMY jenkins@9ad0f1d92378
    # The key's randomart image is:
    # +---[RSA 3072]----+
    # |        . +oo..  |
    # |       . o *E+.  |
    # |        . ++o.+. |
    # |       . ..  *.+ |
    # |      . S . + o.o|
    # |       +   . .o..|
    # |      = .   .ooo+|
    # |     . =     **=o|
    # |      . .    =@=.|
    # +----[SHA256]-----+

# now, I need to copy the jenkins public key which is called 
# my-experiment-key.pub to the remote-host /home/remote_user/.ssh/authorized_keys

# how to copy something inside the container out
# https://support.sitecore.com/kb?id=kb_article_view&sysparm_article=KB0383441 

# docker cp <container>:<src-path> <local-dest-path>  
# or even better I could copy the content from one container to another
# how to copy the contents from one container to another?
# https://medium.com/@gchudnov/copying-data-between-docker-containers-26890935da3f
docker cp jenkins:tmp/my-experiment-key.pub ./my-experiment-key.pub
# this works...
# let's try to copy from one container directly to another
docker cp jenkins:tmp/my-experiment-key.pub remote-host:/home/remote_user/.ssh/my-experiment-key.pub
    # william@william-ThinkPad-T450:~/Documents/statistical-learning/jenkins_course/221009_01$ docker cp jenkins:tmp/my-experiment-key.pub remote-host:/home/remote_user/.ssh/my-experiment-key.pub
    # copying between containers is not supported

# we've hot a problem, we can't copy between containers
# we can solve this problem doing:
docker cp jenkins:tmp/my-experiment-key.pub ./my-experiment-key.pub
docker cp ./my-experiment-key.pub  remote-host:/home/remote_user/.ssh/my-experiment-key.pub
rm ./my-experiment-key.pub

# why do we need to use .ssh/authorized_keys
# https://www.ssh.com/academy/ssh/authorized-keys-file#:~:text=The%20authorized_keys%20file%20in%20SSH,keys%20and%20needs%20proper%20management.
    # The authorized_keys file in SSH specifies the SSH keys that can be used for logging into the user account for which the file is configured. It is a highly important configuration file, as it configures permanent access using SSH keys and needs proper management.

# how to add public key to authorized keys?
# https://www.google.com/search?q=how+to+add+public+key+to+authorized+keys%3F&oq=how+to+add+public+key+to+authorized+keys%3F&aqs=chrome..69i57j0i13i512l2j0i22i30l7.2006j0j4&sourceid=chrome&ie=UTF-8
# enter inside the remote-host container
docker exec -it remote-host bash
# [inside the remote-host container]
cd /home/remote_user/.ssh
ll
    # [root@857cab7f486a .ssh]# ll
    # total 8
    # -rw------- 1 remote_user remote_user 583 Oct 15 02:41 authorized_keys
    # -rw-r--r-- 1 remote_user remote_user 574 Oct 17 13:59 my-experiment-key.pub

# Use the following command: # cat ~root/.ssh/<hostname_1>_id_rsa.pub >> ~root/.ssh/authorized_keys.
cat ./my-experiment-key.pub >> ./authorized_keys
# it worked...
cat ./authorized_keys
    # [root@857cab7f486a .ssh]# cat ./authorized_keys
    # ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCsfP4t9KJeEMj6lXEWZowsDcbDwkCk939FL7l5HxQjKdrp1BQcHKTxLZAMIeis9dBmUrAqZpsMI8Ladh/ZbkAY5oYC+zvHuRDsPDTOY7kZYMzh5H+4oK8k9nT/t2GpzOwQsPm9Fv+5Z/WIHCrBmzaDi6edQ5pnPaclpg7i/mGf1TNBtSlnhGfu1UqpHYx8Tg9sGauMsyTvPuagmaFPoOERG/0/370gOBOAWWOorWIpW5CAJrZibo/H9jRqaetSBYGS/XKikiEty05gP9JpMCHPtlxga4hga9FjreYB6axRN2We80rclg1HgTbYdZcE/s+avSsNmd9K8mJtdrr6yBlERDxQ0o9e1kB/5BrebxKtI21RaJOOjHz4jruT8aLAStZMccGE/dAa2cc89Erga0krwyfxePuhUUQ3wlEsip1N5C3SXlTXjOFhwIXzP9jLxQnOOBJebx/qIWHSoJuRhRE/yzocCRMk7oxirW92rhAyPTfmRPI5xYbO0/6EY7izN4c= william@william-ThinkPad-T450
    # ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCkETolAPaNYzuH1c9je2bCmoAVBXWrUPshD6MzKidZ4JlHoNB7z4vxF9f7CLXCfz7Py9Jjiv11+XsIiEeYBf4IdV/rlHP0z1ZvMpVX8Rc2qn5Gsiy/c6a20jiQAQ8XppdCNX1qZX8nC80VkBNO5Hiao9yYt1rkjcWjxRwsA8SBa+80TZnWQtfoh1oQtWj7I050yu7a70JkqGNdj2vIdDVzOUMcE+wlk3Tb9MzSrL47R9KE95vQ4Xa+8aDwdd5RqGMlTueTFG+otOJpNUzM1V3TT7lcMUqaI4iMbYqpSqODxppC2M3hIaZ2qKL3KJnu/cMwzZ/zvB8JDnTJvOma8ouMFmCO8FgY5ibTdddRlXU0a//AAEAeMqB2KkVupZrywK2ZUnXrCSN5uib0WjsC5MdJ5hHTJLLe8TusrPfA8AWBXM8a4FFZp+czKXGtSSviK+/STZopneqRdja476ZLDa/AahMkwhuQlS9gL7gjg3bztuwxvsigB+wVPFp1vhkJi7c= jenkins@9ad0f1d92378
# note that we have two ssh public keys inside here
# the first one I created from the host machine (my laptop) the other I created from inside the jenkins container

# now we need to test if we can do a ssh from the jenkins container to the 
# remote-host container
# using this new key called my-experiment-key

# enter into the jenkins container
docker exec -it jenkins bash
# [inside the jenkins container]
ssh -i /tmp/my-experiment-key remote_user@remote_host
# use -i to specify the private key used
# and we will ssh as the remote_user
    # jenkins@9ad0f1d92378:/$ ssh -i /tmp/my-experiment-key remote_user@remote_host
    # Warning: Permanently added the ECDSA host key for IP address '172.19.0.2' to the list of known hosts.
    # Last login: Sat Oct 15 03:14:00 2022 from jenkins.221009_01_net
    # [remote_user@857cab7f486a ~]$ 
# It worked!


# =================================================== 
# I'm having trouble with the "can't connect to server jenkins"
# https://linuxbeast.com/tutorials/fixes/jenkins-cant-connect-to-server-using-ssh-remote/
# maybe it because I'm using ECDSA instead of RSA
ssh-keygen -t rsa -m PEM -f my-remote-key-rsa-test
    # william@william-ThinkPad-T450:~/Documents/statistical-learning/jenkins_course/221009_01/centos7$ ssh-keygen -t rsa -m PEM -f my-remote-key-rsa-test
    # Generating public/private rsa key pair.
    # Enter passphrase (empty for no passphrase): 
    # Enter same passphrase again: 
    # Your identification has been saved in my-remote-key-rsa-test
    # Your public key has been saved in my-remote-key-rsa-test.pub
    # The key fingerprint is:
    # SHA256:QAAyrx+SweVaHn8opUDqnPPtilGr240uDhaxZyBVZfo william@william-ThinkPad-T450
    # The key's randomart image is:
    # +---[RSA 3072]----+
    # |o.o+oo+          |
    # |+=o  +           |
    # |+=.+...          |
    # |++X =...         |
    # |+O.B oE.S        |
    # | oB.+ .          |
    # |.o.o .           |
    # |o.= +            |
    # |.=+=.o           |
    # +----[SHA256]-----+


docker cp ./centos7/my-remote-key-rsa-test jenkins:/tmp/my-remote-key-rsa-test

docker cp ./centos7/my-remote-key-rsa-test.pub  remote-host:/home/remote_user/.ssh/my-remote-key-rsa-test.pub

docker exec -it remote-host bash
cd /home/remote_user/.ssh
cat ./my-remote-key-rsa-test.pub >> ./authorized_keys

cat ./authorized_keys
    # [root@857cab7f486a .ssh]# cat ./authorized_keys
    # ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCsfP4t9KJeEMj6lXEWZowsDcbDwkCk939FL7l5HxQjKdrp1BQcHKTxLZAMIeis9dBmUrAqZpsMI8Ladh/ZbkAY5oYC+zvHuRDsPDTOY7kZYMzh5H+4oK8k9nT/t2GpzOwQsPm9Fv+5Z/WIHCrBmzaDi6edQ5pnPaclpg7i/mGf1TNBtSlnhGfu1UqpHYx8Tg9sGauMsyTvPuagmaFPoOERG/0/370gOBOAWWOorWIpW5CAJrZibo/H9jRqaetSBYGS/XKikiEty05gP9JpMCHPtlxga4hga9FjreYB6axRN2We80rclg1HgTbYdZcE/s+avSsNmd9K8mJtdrr6yBlERDxQ0o9e1kB/5BrebxKtI21RaJOOjHz4jruT8aLAStZMccGE/dAa2cc89Erga0krwyfxePuhUUQ3wlEsip1N5C3SXlTXjOFhwIXzP9jLxQnOOBJebx/qIWHSoJuRhRE/yzocCRMk7oxirW92rhAyPTfmRPI5xYbO0/6EY7izN4c= william@william-ThinkPad-T450
    # ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCkETolAPaNYzuH1c9je2bCmoAVBXWrUPshD6MzKidZ4JlHoNB7z4vxF9f7CLXCfz7Py9Jjiv11+XsIiEeYBf4IdV/rlHP0z1ZvMpVX8Rc2qn5Gsiy/c6a20jiQAQ8XppdCNX1qZX8nC80VkBNO5Hiao9yYt1rkjcWjxRwsA8SBa+80TZnWQtfoh1oQtWj7I050yu7a70JkqGNdj2vIdDVzOUMcE+wlk3Tb9MzSrL47R9KE95vQ4Xa+8aDwdd5RqGMlTueTFG+otOJpNUzM1V3TT7lcMUqaI4iMbYqpSqODxppC2M3hIaZ2qKL3KJnu/cMwzZ/zvB8JDnTJvOma8ouMFmCO8FgY5ibTdddRlXU0a//AAEAeMqB2KkVupZrywK2ZUnXrCSN5uib0WjsC5MdJ5hHTJLLe8TusrPfA8AWBXM8a4FFZp+czKXGtSSviK+/STZopneqRdja476ZLDa/AahMkwhuQlS9gL7gjg3bztuwxvsigB+wVPFp1vhkJi7c= jenkins@9ad0f1d92378
    # ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC2HuQcw4l9V0PJ0AlwlVZdg/5iHRDRMqah/dcScHof40wz0mt1cFmHlTR4F1/HkgoPIP+RDaexsJ5olD39STMf68RkQ5P/nPbQMbULfYshvbyBbp8GjluZk7Qy+6TQP0R9P2ZRM3CLKD6oVJ2JqcYR7GtSPQOiEu5U9ITwFlBM8VQa7QtjKnsFx7KI011fnv9ZF1OAgfKqyG/9HQO6dDh8wBwYQCjkv2UD4VFRozOhua2nwCFIFIxvLWLT6p78cxD4dJW4sfwg+RinI5gi8Ijno/ENqoL+C3LJXnT89cK8/Y68adIfI3Ug+fxNaj1wCXo0v/OBFh+rqyUWerAbSo+CUmG5Emth9PmsyIhl9oP4JnwlSfdkqaIU+6LxYzSOvNac9PkH5C3cMzqAofQ1Jif/aVqjZVpDSVAJEoyMrBqGBAFs+fPA8uRc7f6Ep4+bsEdBxaCdq45RZZD01o0PzZSAt36wGa3N8NDXYn1LKa8Fw0NjU/0dEOaad/xFDQ0ka90= william@william-ThinkPad-T450
    # [root@857cab7f486a .ssh]# 

# It seems that all of them are RSA ...
# it worked... strange, but good news
# let's try to use one of the other two, which we did not use "-t rsa option..."
# again it did not work with the usual ssh-keygen 
# but it worked with the ssh-keygen -t rsa

