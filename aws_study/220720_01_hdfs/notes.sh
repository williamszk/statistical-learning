


# C:\Users\william.suzuki\Documents\study\aws_study\aws_personal_ubuntu_server_key.pem

# ssh -i "C:\Users\william.suzuki\Documents\study\aws_study\aws_personal_ubuntu_server_key.pem" ubuntu@ec2-18-230-115-69.sa-east-1.compute.amazonaws.com
ssh -i "C:\Users\william.suzuki\Documents\study\aws_study\aws_personal_ubuntu_server_key.pem" ubuntu@18.228.245.218

# https://www.digitalocean.com/community/tutorials/how-to-install-hadoop-in-stand-alone-mode-on-ubuntu-20-04 

# ------------------------ #
# Inside the EC2 instance
# ------------------------ #

# To get started, you’ll update our package list and install OpenJDK, the default Java Development Kit on Ubuntu 20.04:
sudo apt update
sudo apt install default-jdk -y

# Once the installation is complete, let’s check the version.
java -version


# https://hadoop.apache.org/releases.html

curl -O https://dlcdn.apache.org/hadoop/common/hadoop-3.3.3/hadoop-3.3.3.tar.gz
#  -O, --remote-name   Write output to a file named as the remote file
#      --remote-name-all Use the remote file name for all URLs

# this file contains the sha512
curl -O https://dlcdn.apache.org/hadoop/common/hadoop-3.3.3/hadoop-3.3.3.tar.gz.sha512
cat hadoop-3.3.3.tar.gz.sha512

# Run checksum verification to see if download was not corrupted
shasum -a 512 hadoop-3.3.3.tar.gz
# This command can take some time
# It should be:
# SHA512 (hadoop-3.3.3.tar.gz) = 1f5762682cef3daff8b2379fe7e40efca107bb7e8dcaa4a513e3bc0c082067759dd05d493ec997433dde2c89ea63dbc93aee0bba60045f89d3ec2d3f687f58b3

# ubuntu@ip-172-31-4-29:~$ shasum -a 512 hadoop-3.3.3.tar.gz
# 1f5762682cef3daff8b2379fe7e40efca107bb7e8dcaa4a513e3bc0c082067759dd05d493ec997433dde2c89ea63dbc93aee0bba60045f89d3ec2d3f687f58b3  hadoop-3.3.3.tar.gz

# Now that you’ve verified that the file wasn’t corrupted or changed, you can extract it:
tar -xzvf hadoop-3.3.3.tar.gz
# Use the tar command with the -x flag to extract, -z to uncompress, -v for verbose output, and -f to specify that you’re extracting from a file.


# Finally, you’ll move the extracted files into /usr/local, the appropriate place for locally installed software:
sudo mv hadoop-3.3.3 /usr/local/hadoop

# With the software in place, you’re ready to configure its environment.

# =========================================== # 
# Step 3 — Configuring Hadoop’s Java Home
# =========================================== # 

# Hadoop requires that you set the path to Java, either as an environment variable or in the Hadoop configuration file.

# To find the default Java path
readlink -f /usr/bin/java | sed "s:bin/java::"

# ubuntu@ip-172-31-4-29:~$ readlink -f /usr/bin/java | sed "s:bin/java::"
# /usr/lib/jvm/java-11-openjdk-amd64/

# To begin, open hadoop-env.sh:
sudo vim /usr/local/hadoop/etc/hadoop/hadoop-env.sh

# Option 1: Set a Static Value
#export JAVA_HOME=
# export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/


# =========================================== # 
# Step 4 — Running Hadoop
# =========================================== # 

# Stopped here
# https://www.digitalocean.com/community/tutorials/how-to-install-hadoop-in-stand-alone-mode-on-ubuntu-20-04

# Enter the EC2 instance:
ssh -i "C:\Users\william.suzuki\Documents\study\aws_study\aws_personal_ubuntu_server_key.pem" ubuntu@52.67.114.118

# Now you should be able to run Hadoop:
/usr/local/hadoop/bin/hadoop


mkdir ~/input
cp /usr/local/hadoop/etc/hadoop/*.xml ~/input



/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.3.jar grep ~/input ~/grep_example 'allowed[.]*'

cat ~/grep_example/*

# More tutorials to take a look:
# https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
# https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html
# https://www.digitalocean.com/community/tutorials/how-to-spin-up-a-hadoop-cluster-with-digitalocean-droplets
# 
