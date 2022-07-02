# https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

# https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

# Access key ID
# Secret access key
# AWS Region
# Output format

aws configure


# AWS Region: sa-east-1
# Output format: json

# see if the AWS CLI is configured
aws configservice describe-configuration-recorder-status


# in the home directory there is a file called:
# .aws
# which inside there is a file called configuration
# inside of it there are the configurations of you aws cli


aws sts get-caller-identity
# this will work if the aws config is ok