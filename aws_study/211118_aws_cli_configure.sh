
# The objective of this script is to study the AWS CLI

# how to know the configure files that are available?
aws configure list

#       Name                    Value             Type    Location
#       ----                    -----             ----    --------     
#    profile                <not set>             None    None
# access_key     ****************SGU7 shared-credentials-file
# secret_key     ****************Rm96 shared-credentials-file
#     region                us-east-1      config-file    ~/.aws/config


# to list all profiles:
aws configure list-profiles
# default


# I want to create another configuration to use aws cli in another account
# how to create another profile in aws cli?
# How to configure multiple profiles for AWS CLI
# https://www.simplified.guide/aws/cli/configure-multiple-profiles
# 
# AWS CLI tool, by default, will create a profile called default when you first run the 
# configure option. The default profile will also be used when you run any AWS CLI tools.

# You can configure multiple profiles or accounts for AWS CLI. 
# AWS calls this named profile and you can then switch to any of the profiles or accounts when running the aws commands.

# In the files below we can find the profiles in aws cli
# ~/.aws/config 
# ~/.aws/credentials

cat ~/.aws/config
# [default]
# region = us-east-1
# output = json

cat ~/.aws/credentials
# [default]
# aws_access_key_id = **********GU7
# aws_secret_access_key = *********************Rm96

# the files show the profile that it refers to

# how to list buckets?
aws s3 ls
# 2021-06-07 14:36:05 name-bucket-1
# 2021-06-07 14:23:01 name-bucket-2
# 2021-01-18 06:18:20 name-bucket-3

# Run aws configure with --profile option and a name for the new profile.
aws configure --profile william_personal_aws


aws configure list-profiles
# default
# william_personal_aws

aws configure list

# Maybe aws configure list only shows info about the account that is currently 
# logged in
aws configure list
#       Name                    Value             Type    Location
#       ----                    -----             ----    --------     
#    profile                <not set>             None    None
# access_key     ****************SGU7 shared-credentials-file
# secret_key     ****************Rm96 shared-credentials-file
#     region                us-east-1      config-file    ~/.aws/config


# how to configure aws cli
# https://www.simplified.guide/aws/cli/configure-on-linux-macos


# ---------------------------------- #
# How to switch profiles on AWS CLI  #
# ---------------------------------- #

aws s3 ls --profile william_personal_aws

# 2021-11-18 16:07:15 library-williamsuzuki
# 2021-04-19 12:40:50 my-aws-bucket-210419

# https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html


aws ec2 describe-instances --profile william_personal_aws
# {
#     "Reservations": [
#         {
#             "Groups": [],
#             "Instances": [
#                 {
#                     "AmiLaunchIndex": 0,
#                     "ImageId": "ami-07bfd9965e7b972d1",
#                     "InstanceId": "i-0d283864772def0d8",
#                     "InstanceType": "t2.micro",
#                     "KeyName": "thinkpad key ec2 tutorial",
#                     "LaunchTime": "2021-11-17T19:05:54+00:00",
#                     "Monitoring": {
#                         "State": "disabled"
#                     },
#                     "Placement": {
# ................

# The return format depends on the format that we set on the
# AWS profile


# To use a named profile for multiple commands, you can avoid specifying 
# the profile in every command by setting the AWS_PROFILE environment variable 
# at the command line.

#$ 
# Linux or macOS
export AWS_PROFILE=william_personal_aws

# Windows
setx AWS_PROFILE william_personal_aws

aws s3 ls

aws s3 ls --profile william_personal_aws


# aws cli how to upload a file from local to s3
# https://qiita.com/alokrawat050/items/56820afdb6968deec6a2

aws s3 ls --profile william_personal_aws
aws s3 ls s3://library-williamsuzuki --profile william_personal_aws

# Creating Buckets
# command "make bucket" = mb
aws s3 mb s3://test-create-bucket-awscli --profile william_personal_aws
# make_bucket: test-create-bucket-awscli

aws s3 ls --profile william_personal_aws
# 2021-11-18 16:07:15 library-williamsuzuki
# 2021-04-19 12:40:50 my-aws-bucket-210419
# 2021-11-18 17:31:59 test-create-bucket-awscli

# To remove a bucket, use the aws s3 rb command.
aws s3 rb s3://test-create-bucket-awscli --profile william_personal_aws
# remove_bucket: test-create-bucket-awscli

aws s3 ls --profile william_personal_aws
# 2021-11-18 16:07:15 library-williamsuzuki
# 2021-04-19 12:40:50 my-aws-bucket-210419
# notice that the bucket is not there anymore

# By default, the bucket must be empty for the operation to succeed. 
# To remove a non-empty bucket, you need to include the --force option.
aws s3 rb s3://<bucket-name> --force

# Copy multiple files from directory
aws s3 cp <your directory path> s3://<your bucket name> --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers --recursive

aws s3 cp "C:\Users\william.suzuki\Documents\test-send-aws-s3\Brian Ward - How Linux works What every superuser should know.pdf" "s3://library-williamsuzuki/Brian Ward - How Linux works What every superuser should know.pdf" --profile william_personal_aws

aws s3 ls "s3://library-williamsuzuki" --profile william_personal_aws
# 2021-11-18 17:42:48    5314521 Brian Ward - How Linux works What every superuser should know.pdf
# the upload was successful, I defeated waterfall!

# aws cli copy but without replacing

cd "C:\Users\william.suzuki\Documents\test-send-aws-s3"
cd "C:\Users\william.suzuki"
aws s3 cp "C:\Users\william.suzuki\Documents\test-send-aws-s3" "s3://library-williamsuzuki" --profile william_personal_aws

aws s3 ls s3://library-williamsuzuki --profile william_personal_aws --human-readable

# build a program that reads the content of s3 bucket library-williamsuzuki
# then sees which are the 

