
# check if aws cli is configured
aws configservice describe-configuration-recorder-status

# An error occurred (UnrecognizedClientException) when calling the DescribeConfigurationRecorderStatus operation: The security token included in the request is invalid.

# How to configure aws cli?


aws ecr get-login-password --region sa-east-1

docker login
# This will login the AWS account of ECR into your Docker Client
aws ecr get-login-password --region sa-east-1 | docker login --username AWS --password-stdin 613363943992.dkr.ecr.sa-east-1.amazonaws.com
# Login Succeeded

# Now the Docker Client is authenticated to the AWS ECR of your account

# Build your Docker image using the following command. 
docker build -t my-node-app:1.0 .

# After the build completes, tag your image so you can push the image to this repository:
docker tag my-node-app:1.0 613363943992.dkr.ecr.sa-east-1.amazonaws.com/my-node-app:1.0

# Run the following command to push this image to your newly created AWS repository:
docker push 613363943992.dkr.ecr.sa-east-1.amazonaws.com/my-node-app:1.0
# The push refers to repository [613363943992.dkr.ecr.sa-east-1.amazonaws.com/my-node-app]
# 8a90eb29a9d5: Pushed 
# c831f9be6869: Pushed 
# 6df21c206587: Pushed 
# d0baefd97422: Pushed 
# 92c140f8363b: Pushed 
# cc7cd04ea96f: Pushed 
# 24302eb7d908: Pushed 
# latest: digest: sha256:f8ab924525fd63b197a1dbe577506806dc3989c93f44a138c3c0ee22b4679b35 size: 1787



