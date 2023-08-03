# about node ------------------------------------------------------------------
# https://expressjs.com/en/starter/generator.html
npm init -y



# about elastic beanstalk in cli ---------------------------------------------- 
pip3 install awscli 
pip3 install awsebcli

eb --version
# EB CLI 3.20.7 (Python 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0])


# eb for elastic beanstalk
eb init

# we can see the credentials for the key using
# cat ~/.aws/config 
# >>>
# [profile eb-cli]
# aws_access_key_id = **********************
# aws_secret_access_key = ****************************

eb create delete-me-application-eb-env

# after some processing
eb deploy

# then we can check with open
eb open









