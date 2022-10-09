# ssh -i "C:\Users\william.suzuki\Documents\study\aws_study\aws_personal_ubuntu_server_key.pem" ubuntu@ec2-18-230-115-69.sa-east-1.compute.amazonaws.com

# https://www.udemy.com/course/learn-devops-the-complete-kubernetes-course/learn/lecture/10576968#questions
# we can install kubernete directly into docker

kubectl get nodes
# The connection to the server localhost:8080 was refused - did you specify the right host or port?

docker ps -a

minikube start

kubectl get nodes
# NAME       STATUS   ROLES                  AGE   VERSION
# minikube   Ready    control-plane,master   11d   v1.22.2


kubectl config get-contexts
# CURRENT   NAME       CLUSTER    AUTHINFO   NAMESPACE
# *         minikube   minikube   minikube   default

# for kubectl we can have many contexts, and we can change the context
# for now we use minikube for study
# but to change context we can use the command:
# kubectl config use-context <name-context>

kubectl get nodes


# kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.4 
kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.4 --port=8080
# pod/hello-minikube created

kubectl expose deployment hello-kubernetes --type=NodePort
# Error from server (NotFound): deployments.apps "hello-kubernetes" not found

kubectl get service hello-kubernetes
# NAME               TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
# hello-kubernetes   NodePort   10.103.75.153   <none>        8080:32663/TCP   11d
# we should use local tunnel to expose this local port to the internet
# so we can access this web page







