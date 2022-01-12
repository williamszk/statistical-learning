# https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c02/learn/lecture/26097978#overview

# https://infrastructure.aws
# AWS regions
# AWS availability zones
# AWS Data Centers
# AWS Edge Locations / Points of Reference

# regions have names
# us-east-1
# eu-west-3
# sa-east-1

# most services are associated with a certain region
# 
# which region to choose?
# compliance: legislation or enterprise
# proximity to reduce latency
# available services, some regions don't have all services
# pricing: it varies depending on the region
# 

# availability zones
# usually there are 3, some have 2 and the max is 6

# Region in Sydney:
# ap-southeast-2

# the availability zones are:
# ap-southeast-2a
# ap-southeast-2b
# ap-southeast-2c

# each have redundant power, networking 
# the availability zones are all connected with high bandwidth with low latency
#

# https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c02/learn/lecture/26097980#overview

# https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c02/learn/lecture/26098112#overview

# EC2 User Data: is the script when we lauch a new instance of EC2

# BOOTSTRAPING means execute commands when the machine starts
# EC2 user data runs with the root user

# https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c02/learn/lecture/26098122#overview

# AMI
# Amazon Machine Image
# the operating system

# ec2 user data
# this is run only one time, when we create the instance
# ---------------------------- # 
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html
# ---------------------------- # 

# to connect to the ec2 instance
ssh -i "~/Documents/aws_some_notes/thinkpadkeyec2tutorial.pem" ec2-user@ec2-18-231-195-76.sa-east-1.compute.amazonaws.com

http://18.231.195.76


ssh -i "~/Documents/aws_some_notes/thinkpadkeyec2tutorial.pem" ec2-user@ec2-18-231-187-209.sa-east-1.compute.amazonaws.com
http://18.231.187.209















