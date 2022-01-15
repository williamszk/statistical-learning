# https://clickhouse.com/docs/en/getting-started/tutorial/
# we are following this tutorial
# I'm going to try to set a container to install the clickHouse stuff

# https://clickhouse.com/docs/en/getting-started/tutorial/

# first I need to see if docker is running in my machine
# I could use a VM in the cloud...

systemctl status docker

docker ps -a

# how to delete all containers in your machine?
docker rm 

docker ps -a | awk '{print $1}'
# CONTAINER
# 02e52aa43997
# 29308cdc1d84
# b353609e4848

# exclude the first line of output and then take the first column
docker ps -a | awk 'NR != 1 {print}' | awk '{print $1}'
# 02e52aa43997
# 29308cdc1d84
# b353609e4848

# set the docker ids as a variable
docker_ids=$(docker ps -a | awk 'NR != 1 {print}' | awk '{print $1}')

# we can see that the ids were captured using the variable assignment
echo $docker_ids
# 02e52aa43997 29308cdc1d84 b353609e4848

docker rm $docker_ids

docker ps -a
# we can see that all containers were deleted

# start and enter a ubuntu container
docker run -it ubuntu /bin/bash

# ubuntu how to see ram
lshw -c memory
echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE) / (1024 * 1024)))
# 7648

# installing ClickHouse in the ubuntu container
# https://clickhouse.com/docs/en/getting-started/tutorial/#single-node-setup
# first thing you do after installing a new linux
apt update
apt install apt-transport-https ca-certificates dirmngr

df -h
# root@2becc6d8ccd6:/# df -h
# Filesystem      Size  Used Avail Use% Mounted on
# overlay         239G   65G  163G  29% /
# tmpfs            64M     0   64M   0% /dev
# tmpfs           3.8G     0  3.8G   0% /sys/fs/cgroup
# shm              64M     0   64M   0% /dev/shm
# /dev/sda6       239G   65G  163G  29% /etc/hosts
# tmpfs           3.8G     0  3.8G   0% /proc/asound
# tmpfs           3.8G     0  3.8G   0% /proc/acpi
# tmpfs           3.8G     0  3.8G   0% /proc/scsi
# tmpfs           3.8G     0  3.8G   0% /sys/firmware


apt install gnupg1
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E0C56BD4

echo "deb https://repo.clickhouse.com/deb/stable/ main/" | tee \
    /etc/apt/sources.list.d/clickhouse.list

apt-get update

# here is where we install clickhouse-server and clickhouse-client
apt-get install -y clickhouse-server clickhouse-client

# password for clickhouse in ubuntu container
# 2becc6d8ccd6
# we shouldn't use a password for the server

# start the daemon of clickhouse-server
service clickhouse-server start
# root@2becc6d8ccd6:/# service clickhouse-server start
#  chown -R clickhouse: '/var/run/clickhouse-server/'
# Will run su -s /bin/sh 'clickhouse' -c '/usr/bin/clickhouse-server --config-file /etc/clickhouse-server/config.xml --pid-file /var/run/clickhouse-server/clickhouse-server.pid --daemon'
# Waiting for server to start
# Waiting for server to start
# Server started

# now we can start the clickhouse client
clickhouse-client

# root@2becc6d8ccd6:/# clickhouse-client
# ClickHouse client version 21.12.3.32 (official build).
# Connecting to localhost:9000 as user default.

# If you have installed ClickHouse and forgot password you can reset it in the configuration file.
# The password for default user is typically located at /etc/clickhouse-server/users.d/default-password.xml
# and deleting this file will reset the password.
# See also /etc/clickhouse-server/users.xml on the server where ClickHouse is installed.

# Code: 516. DB::Exception: Received from localhost:9000. DB::Exception: default: Authentication failed: password is incorrect or there is no user with such name. (AUTHENTICATION_FAILED)

# I deleted the file as indicated on the text above

clickhouse-client
# root@2becc6d8ccd6:/# clickhouse-client
# ClickHouse client version 21.12.3.32 (official build).
# Connecting to localhost:9000 as user default.
# Connected to ClickHouse server version 21.12.3 revision 54452.

# 2becc6d8ccd6 :) 

# the dafault place where the clickhouse database is installed:
# the default value is /var/lib/clickhouse/

# The default location for server logs is /var/log/clickhouse-server/.

# Once the clickhouse-server is up and running, we can use clickhouse-client to connect to the 
# server and run some test queries like SELECT "Hello, world!";.

# SELECT `Hello, world!`

# Query id: 696d01de-6d4a-41e1-8b43-ca9786b9351c


# 0 rows in set. Elapsed: 0.002 sec. 

# Received exception from server (version 21.12.3):
# Code: 47. DB::Exception: Received from localhost:9000. DB::Exception: Missing columns: 
# 'Hello, world!' while processing query: 'SELECT `Hello, world!`', required columns: 'Hello, world!'. (UNKNOWN_IDENTIFIER)



# alternative ways to use clickhouse in interactive way:
clickhouse-client
clickhouse-client --host=... --port=... --user=... --password=...

# Run queries in batch-mode:
clickhouse-client --query='SELECT 1'
echo 'SELECT 1' | clickhouse-client
clickhouse-client <<< 'SELECT 1'


# Insert data from a file in specified format:
clickhouse-client --query='INSERT INTO table VALUES' < data.txt
clickhouse-client --query='INSERT INTO table FORMAT TabSeparated' < data.tsv

# Now we use real data 
# https://clickhouse.com/docs/en/getting-started/tutorial/#download-and-extract-table-data

# lets download the files in a dedicated directory
cd ~
mkdir clickhouseTutorial
cd clickhouseTutorial

# we got some errors
# bash: curl: command not found
# bash: unxz: command not found

# we need to install curl and xz-utils
apt install curl xz-utils
# I think it will work now

# what is tsv format?
# Tab-separated values

# here we donwload 2 tsv files
# - hits_v1.tsv
# - visits_v1.tsv

# this takes less than 10min
curl https://datasets.clickhouse.com/hits/tsv/hits_v1.tsv.xz | unxz --threads=`nproc` > hits_v1.tsv
curl https://datasets.clickhouse.com/visits/tsv/visits_v1.tsv.xz | unxz --threads=`nproc` > visits_v1.tsv

root@2becc6d8ccd6:~/clickhouseTutorial# curl https://datasets.clickhouse.com/hits/tsv/hits_v1.tsv.xz | unxz --threads=`nproc` > hits_v1.tsv
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  802M  100  802M    0     0  3870k      0  0:03:32  0:03:32 --:--:-- 3751k

# finish downloading the .tsv files
# I'll try to exit the container and then return to the server again

docker ps -a
# CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                      PORTS     NAMES
# 2becc6d8ccd6   ubuntu    "/bin/bash"   48 minutes ago   Exited (0) 13 seconds ago             interesting_villani

# we need to start the container first and then we go inside of it using exec -it
docker start interesting_villani
docker exec -it interesting_villani /bin/bash
# root@2becc6d8ccd6:/# 

# another test
docker ps -a
# CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS         PORTS     NAMES
# 2becc6d8ccd6   ubuntu    "/bin/bash"   53 minutes ago   Up 3 minutes             interesting_villani

docker stop interesting_villani

docker ps -a
# CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                     PORTS     NAMES
# 2becc6d8ccd6   ubuntu    "/bin/bash"   54 minutes ago   Exited (0) 4 seconds ago             interesting_villani

docker start interesting_villani
docker exec -it interesting_villani /bin/bash

# and then we can get inside the docker container
# root@2becc6d8ccd6:/# 

# see if clickhouse-server is running
service clickhouse-server status

# root@2becc6d8ccd6:/# service clickhouse-server status
# /var/run/clickhouse-server/clickhouse-server.pid file exists and contains pid = 3594.
# The process with pid = 3594 does not exist.

# It seems that the service did not start.

service clickhouse-server start

# root@2becc6d8ccd6:/# service clickhouse-server start
# /var/run/clickhouse-server/clickhouse-server.pid file exists and contains pid = 3594.
# Will run su -s /bin/sh 'clickhouse' -c '/usr/bin/clickhouse-server --config-file /etc/clickhouse-server/config.xml --pid-file /var/run/clickhouse-server/clickhouse-server.pid --daemon'
# Waiting for server to start
# Server started

# start clickhouse-client in interactive mode
clickhouse-client

# root@2becc6d8ccd6:/# clickhouse-client
# ClickHouse client version 21.12.3.32 (official build).
# Connecting to localhost:9000 as user default.
# Connected to ClickHouse server version 21.12.3 revision 54452.

# 2becc6d8ccd6 :) 














