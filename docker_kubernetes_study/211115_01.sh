# ssh -i "C:\Users\william.suzuki\Documents\study\aws_study\aws_personal_ubuntu_server_key.pem" ubuntu@ec2-18-230-115-69.sa-east-1.compute.amazonaws.com

# when in a machine that has minikube installed
minikube start

# the installation of kubectl is independent from minikube
# check if kubectl is already installed
kubectl version
# there is kubectl for client and for server

docker ps -a

# what is kubeadm?

# where is the configuration file for minikube?
cat ~/.kube/config

# we use kubectl to interact with a kubernetes cluster


kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.4

minikube service list

minikube service hello-minikube


minikube stop

minikube delete



