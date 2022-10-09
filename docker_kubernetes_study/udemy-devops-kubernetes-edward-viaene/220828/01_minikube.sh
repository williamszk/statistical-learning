
# install minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

minikube
# william@william-300E5M-300E5L:~/Documents/statistical-learning/docker_kubernetes_study$ minikube
# minikube provisions and manages local Kubernetes clusters optimized for development workflows.

# Basic Commands:
#   start            Starts a local Kubernetes cluster
#   status           Gets the status of a local Kubernetes cluster
#   stop             Stops a running local Kubernetes cluster
#   delete           Deletes a local Kubernetes cluster
#   dashboard        Access the Kubernetes dashboard running within the minikube cluster
#   pause            pause Kubernetes
#   unpause          unpause Kubernetes

minikube start

kubectl
# Command 'kubectl' not found, but can be installed with:
# sudo snap install kubectl

# https://stackoverflow.com/a/63690859/8782077
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

kubectl cluster-info
kubectl version

# kubectl cluster-info
# Kubernetes control plane is running at https://192.168.49.2:8443
# CoreDNS is running at https://192.168.49.2:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
# To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

# kubectl version
# WARNING: This version information is deprecated and will be replaced with the output from kubectl version --short.  Use --output=yaml|json to get the full version.
# Client Version: version.Info{Major:"1", Minor:"25", GitVersion:"v1.25.0", GitCommit:"a866cbe2e5bbaa01cfd5e969aa3e033f3282a8a2", GitTreeState:"clean", BuildDate:"2022-08-23T17:44:59Z", GoVersion:"go1.19", Compiler:"gc", Platform:"linux/amd64"}
# Kustomize Version: v4.5.7
# Server Version: version.Info{Major:"1", Minor:"24", GitVersion:"v1.24.3", GitCommit:"aef86a93758dc3cb2c658dd9657ab4ad4afc21cb", GitTreeState:"clean", BuildDate:"2022-07-13T14:23:26Z", GoVersion:"go1.18.3", Compiler:"gc", Platform:"linux/amd64"}


minikube stop
# ✋  Stopping node "minikube"  ...
# 🛑  Powering off "minikube" via SSH ...
# 🛑  1 node stopped.

minikube start
# 😄  minikube v1.26.1 on Ubuntu 20.04
# ✨  Using the docker driver based on existing profile
# 👍  Starting control plane node minikube in cluster minikube
# 🚜  Pulling base image ...
# 🤷  docker "minikube" container is missing, will recreate.
# 🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
# 🐳  Preparing Kubernetes v1.24.3 on Docker 20.10.17 ...
# 🔎  Verifying Kubernetes components...
#     ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
# 🌟  Enabled addons: storage-provisioner, default-storageclass
# 🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default


# notice we are using Kubernetes 1.24

# minikube create a config file
cat ~/.kube/config
# apiVersion: v1
# clusters:
# - cluster:
#     certificate-authority: /home/william/.minikube/ca.crt
#     extensions:
#     - extension:
#         last-update: Sun, 28 Aug 2022 15:01:52 -03
#         provider: minikube.sigs.k8s.io
#         version: v1.26.1
#       name: cluster_info
#     server: https://192.168.49.2:8443
#   name: minikube
# contexts:
# - context:
#     cluster: minikube
#     extensions:
#     - extension:
#         last-update: Sun, 28 Aug 2022 15:01:52 -03
#         provider: minikube.sigs.k8s.io
#         version: v1.26.1
#       name: context_info
#     namespace: default
#     user: minikube
#   name: minikube
# current-context: minikube
# kind: Config
# preferences: {}
# users:
# - name: minikube
#   user:
#     client-certificate: /home/william/.minikube/profiles/minikube/client.crt
#     client-key: /home/william/.minikube/profiles/minikube/client.key


# what are deployments and services?

kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.4
# deployment.apps/hello-minikube created

# to list all deployments
kubectl get deployments
# NAME             READY   UP-TO-DATE   AVAILABLE   AGE
# hello-minikube   1/1     1            1           60s

# explose the deploymnet
kubectl expose deployment hello-minikube --type=NodePort --port=8080
# service/hello-minikube exposed

minikube service hello-minikube
# |-----------|----------------|-------------|---------------------------|
# | NAMESPACE |      NAME      | TARGET PORT |            URL            |
# |-----------|----------------|-------------|---------------------------|
# | default   | hello-minikube |        8080 | http://192.168.49.2:32766 |
# |-----------|----------------|-------------|---------------------------|
# 🎉  Opening service default/hello-minikube in default browser...


docker ps -a
# CONTAINER ID   IMAGE                                 COMMAND                  CREATED        STATUS                    PORTS                                                                                                                                  NAMES
# beb7f638cd4d   gcr.io/k8s-minikube/kicbase:v0.0.33   "/usr/local/bin/entr…"   4 hours ago    Up 4 hours                127.0.0.1:49162->22/tcp, 127.0.0.1:49161->2376/tcp, 127.0.0.1:49160->5000/tcp, 127.0.0.1:49159->8443/tcp, 127.0.0.1:49158->32443/tcp   minikube

minikube stop
# ✋  Stopping node "minikube"  ...
# 🛑  Powering off "minikube" via SSH ...
# 🛑  1 node stopped.


docker ps -a
# CONTAINER ID   IMAGE                                 COMMAND                  CREATED        STATUS                        PORTS     NAMES
# beb7f638cd4d   gcr.io/k8s-minikube/kicbase:v0.0.33   "/usr/local/bin/entr…"   4 hours ago    Exited (130) 38 seconds ago             minikube


cat ~/.kube/config
# apiVersion: v1
# clusters: null
# contexts: null
# current-context: ""
# kind: Config
# preferences: {}
# users: null


# this will delete the profile of minikube also?
minikube delete
# 🔥  Deleting "minikube" in docker ...
# 🔥  Deleting container "minikube" ...
# 🔥  Removing /home/william/.minikube/machines/minikube ...
# 💀  Removed all traces of the "minikube" cluster.



cat ~/.kube/config
# apiVersion: v1
# clusters: null
# contexts: null
# current-context: ""
# kind: Config
# preferences: {}
# users: null


docker ps -a
# there is no more container of minikube


