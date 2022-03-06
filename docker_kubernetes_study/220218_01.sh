# https://www.youtube.com/watch?v=d6WC5n9G_sM&ab_channel=freeCodeCamp.org
# kubernetes course
# we can run kubernetes without dokcer
# other alternative for container services are:
# containerd and CRI-O

# container orchestration system

# minikube
# kubectl
# vscode

# https://kubernetes.io/
# https://kubernetes.io/docs/setup/
# https://kubernetes.io/docs/tutorials/

# see if minikube is already installed
# https://minikube.sigs.k8s.io/docs/start/


# see if kubectl is already installed
kubectl cluster-info

# curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/OS_DISTRIBUTION/amd64/kubectl
# chmod +x ./kubectl
# sudo mv ./kubectl /usr/local/bin/kubectl

# sudo snap install kubectl

# kubectl version

# https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

kubectl version --client

kubectl cluster-info

# there is other tool called "kind" that let us study kubernetes locally
# but we'll use minikube
# https://minikube.sigs.k8s.io/docs/start/

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

minikube start

minikube help
# Basic Commands:
#   start          Starts a local Kubernetes cluster
#   status         Gets the status of a local Kubernetes cluster
#   stop           Stops a running local Kubernetes cluster
#   delete         Deletes a local Kubernetes cluster
#   dashboard      Access the Kubernetes dashboard running within the minikube cluster
#   pause          pause Kubernetes
#   unpause        unpause Kubernetes


# https://youtu.be/d6WC5n9G_sM?t=1770

minikube status
# minikube
# type: Control Plane
# host: Running
# kubelet: Running
# apiserver: Running
# kubeconfig: Configured

minikube ip
# 192.168.49.2
# the ip of the kubernetes cluster

# we need to ssh into the minikube cluster
# ssh docker@192.168.49.2
# default password
# tcuser
# in the case of docker based minikube just use:
minikube ssh

# inside minikube server
docker ps

# docker is the default container runtime for kubernetes
# but we can use other container runtime programs

# CONTAINER ID    NAMES
# d159d639b107    k8s_storage-provisioner_storage-provisioner_kube-system_d01e85c3-4d2a-4b06-ac66-96c15205740f_1
# 6a857a7f828f    k8s_coredns_coredns-64897985d-5tw6q_kube-system_b6b312a1-a3ba-4fe2-8c83-c425536b486e_0
# d1cf8540e387    k8s_kube-proxy_kube-proxy-bhdtn_kube-system_5fccf96c-e440-43e8-aa39-c9eca361a3ed_0
# 7a218930a044    k8s_POD_kube-proxy-bhdtn_kube-system_5fccf96c-e440-43e8-aa39-c9eca361a3ed_0
# d7b60ad67ebc    k8s_POD_coredns-64897985d-5tw6q_kube-system_b6b312a1-a3ba-4fe2-8c83-c425536b486e_0
# 7786b622e865    k8s_POD_storage-provisioner_kube-system_d01e85c3-4d2a-4b06-ac66-96c15205740f_0
# 8d543fb93391    k8s_kube-scheduler_kube-scheduler-minikube_kube-system_b8bdc344ff0000e961009344b94de59c_0
# f96da7ba7809    k8s_kube-apiserver_kube-apiserver-minikube_kube-system_96be69ce9ff7dc0acff6fda2873a009a_0
# bf75909abad9    k8s_etcd_etcd-minikube_kube-system_9d3d310935e5fabe942511eec3e2cd0c_0
# 9814c875dea1    k8s_kube-controller-manager_kube-controller-manager-minikube_kube-system_3db91997554714e5ece3296773cf98a5_0
# fced11c841c9    k8s_POD_kube-apiserver-minikube_kube-system_96be69ce9ff7dc0acff6fda2873a009a_0
# 8bc1b0387ff6    k8s_POD_etcd-minikube_kube-system_9d3d310935e5fabe942511eec3e2cd0c_0
# a8d8cb27a05f    k8s_POD_kube-scheduler-minikube_kube-system_b8bdc344ff0000e961009344b94de59c_0
# 16a847550d6b    k8s_POD_kube-controller-manager-minikube_kube-system_3db91997554714e5ece3296773cf98a5_0

# kubectl is not available inside the kubernetes node
# kubectl is an external tool used to manage a k8s cluster

exit
# docker@minikube:~$ exit
# logout

# exited k8s cluster

kubectl version
# Client Version: version.Info{Major:"1", Minor:"23", GitVersion:"v1.23.4", GitCommit:"e6c093d87ea4cbb530a7b2ae91e54c0842d8308a", GitTreeState:"clean", BuildDate:"2022-02-16T12:38:05Z", GoVersion:"go1.17.7", Compiler:"gc", Platform:"linux/amd64"}
# Server Version: version.Info{Major:"1", Minor:"23", GitVersion:"v1.23.1", GitCommit:"86ec240af8cbd1b60bcc4c03c20da9b98005b92e", GitTreeState:"clean", BuildDate:"2021-12-16T11:34:54Z", GoVersion:"go1.17.5", Compiler:"gc", Platform:"linux/amd64"}

kubectl cluster-info
# Kubernetes control plane is running at https://192.168.49.2:8443
# CoreDNS is running at https://192.168.49.2:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
# To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

kubectl get nodes
# NAME       STATUS   ROLES                  AGE   VERSION
# minikube   Ready    control-plane,master   31m   v1.23.1

kubectl get pods
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ kubectl get pods
# No resources found in default namespace.

kubectl get namespaces
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ kubectl get namespaces
# NAME              STATUS   AGE
# default           Active   33m
# kube-node-lease   Active   33m
# kube-public       Active   33m
# kube-system       Active   33m

# there are many namespaces where pods live

kubectl get pods --namespace=kube-system
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ kubectl get pods --namespace=kube-system
# NAME                               READY   STATUS    RESTARTS      AGE
# coredns-64897985d-5tw6q            1/1     Running   0             34m
# etcd-minikube                      1/1     Running   0             35m
# kube-apiserver-minikube            1/1     Running   0             35m
# kube-controller-manager-minikube   1/1     Running   0             35m
# kube-proxy-bhdtn                   1/1     Running   0             34m
# kube-scheduler-minikube            1/1     Running   0             35m
# storage-provisioner                1/1     Running   1 (34m ago)   35m

# next:
# https://youtu.be/d6WC5n9G_sM?t=2438
# how to create pods manually

# create a pod with name mypod-nginx with image nginx
kubectl run mypod-nginx --image=nginx
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ kubectl run mypod-nginx --image=nginx
# pod/mypod-nginx created

kubectl get pods
# NAME          READY   STATUS              RESTARTS   AGE
# mypod-nginx   0/1     ContainerCreating   0          21s

kubectl get pods
# NAME          READY   STATUS    RESTARTS   AGE
# mypod-nginx   1/1     Running   0          79s

kubectl describe pod mypod-nginx
# Name:         mypod-nginx
# Namespace:    default
# Priority:     0
# Node:         minikube/192.168.49.2
# Start Time:   Mon, 21 Feb 2022 00:54:18 -0300
# Labels:       run=mypod-nginx
# Annotations:  <none>
# Status:       Running
# IP:           172.17.0.3
# IPs:
#   IP:  172.17.0.3
# Containers:
#   mypod-nginx:
#     Container ID:   docker://47620962b509a7174ca7c641492e1081a0645ebc8a7b6f6c40fed3482b7e647d
#     Image:          nginx
#     Image ID:       docker-pullable://nginx@sha256:2834dc507516af02784808c5f48b7cbe38b8ed5d0f4837f16e78d00deb7e7767
#     Port:           <none>
#     Host Port:      <none>
#     State:          Running
#       Started:      Mon, 21 Feb 2022 00:55:00 -0300
#     Ready:          True
#     Restart Count:  0
#     Environment:    <none>
#     Mounts:
#       /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-s89wf (ro)
# Conditions:
#   Type              Status
#   Initialized       True 
#   Ready             True 
#   ContainersReady   True 
#   PodScheduled      True 
# Volumes:
#   kube-api-access-s89wf:
#     Type:                    Projected (a volume that contains injected data from multiple sources)
#     TokenExpirationSeconds:  3607
#     ConfigMapName:           kube-root-ca.crt
#     ConfigMapOptional:       <nil>
#     DownwardAPI:             true
# QoS Class:                   BestEffort
# Node-Selectors:              <none>
# Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
#                              node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
# Events:
#   Type    Reason     Age    From               Message
#   ----    ------     ----   ----               -------
#   Normal  Scheduled  2m32s  default-scheduler  Successfully assigned default/mypod-nginx to minikube
#   Normal  Pulling    2m29s  kubelet            Pulling image "nginx"
#   Normal  Pulled     113s   kubelet            Successfully pulled image "nginx" in 35.057768521s
#   Normal  Created    109s   kubelet            Created container mypod-nginx
#   Normal  Started    108s   kubelet            Started container mypod-nginx


kubectl get pods
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ kubectl get pods
# NAME          READY   STATUS    RESTARTS   AGE
# mypod-nginx   1/1     Running   0          7m14s

# enter again into the cluster
minikube ssh
docker ps | grep mypod-nginx
# docker@minikube:~$ docker ps | grep mypod-nginx
# CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS         PORTS     NAMES
# 47620962b509   nginx                  "/docker-entrypoint.…"   7 minutes ago   Up 7 minutes             k8s_mypod-nginx_mypod-nginx_default_3cb5e320-fcda-4376-8f5e-071fd0cf27c3_0
# d40ab3ae28e5   k8s.gcr.io/pause:3.6   "/pause"                 8 minutes ago   Up 8 minutes             k8s_POD_mypod-nginx_default_3cb5e320-fcda-4376-8f5e-071fd0cf27c3_0

# we'll connect to the nginx container
# (this container is running inside a pod in minikube)
docker exec -it 47620962b509 sh

# [inside container 47620962b509]
hostname
# # hostname
# mypod-nginx

# check ip address of the container
hostname -i
# # hostname -i
# 172.17.0.3

# let's try to make a request to this ip address
# note that we are inside the nginx container
curl 172.17.0.3
# curl 172.17.0.3
# <!DOCTYPE html>
# <html>
# <head>
# <title>Welcome to nginx!</title>
# <style>
# html { color-scheme: light dark; }
# body { width: 35em; margin: 0 auto;
# font-family: Tahoma, Verdana, Arial, sans-serif; }
# </style>
# </head>
# <body>
# <h1>Welcome to nginx!</h1>
# <p>If you see this page, the nginx web server is successfully installed and
# working. Further configuration is required.</p>

# <p>For online documentation and support please refer to
# <a href="http://nginx.org/">nginx.org</a>.<br/>
# Commercial support is available at
# <a href="http://nginx.com/">nginx.com</a>.</p>

# <p><em>Thank you for using nginx.</em></p>
# </body>
# </html>

# exit container
# [inside the minikube cluster]
# exit ssh to the cluster
# [in the usual terminal]

kubectl get pods -o wide
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ kubectl get pods -o wide
# NAME          READY   STATUS    RESTARTS   AGE   IP           NODE       NOMINATED NODE   READINESS GATES
# mypod-nginx   1/1     Running   0          16m   172.17.0.3   minikube   <none>           <none>

# delete the pod that we created
kubectl delete pod mypod-nginx
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ kubectl delete pod mypod-nginx
# pod "mypod-nginx" deleted

kubectl get pods
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ kubectl get pods
# No resources found in default namespace.

# next
# https://www.youtube.com/watch?v=d6WC5n9G_sM&t=3164s&ab_channel=freeCodeCamp.org
# alias to kubectl
# to type less
# k
k get pods
# docker@minikube:~$ k get pods
# -bash: k: command not found

alias k="kubectl"

k get pods
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k get pods
# No resources found in default namespace.

# next
# https://www.youtube.com/watch?v=d6WC5n9G_sM&t=3317s&ab_channel=freeCodeCamp.org
# creating and exploring deployment

k create deployment mydeployment --image=nginx
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k create deployment mydeployment --image=nginx
# deployment.apps/mydeployment created

k get deployments
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k get deployments
# NAME           READY   UP-TO-DATE   AVAILABLE   AGE
# mydeployment   1/1     1            1           24s

k get pods
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k get pods
# NAME                            READY   STATUS    RESTARTS   AGE
# mydeployment-84777db489-4cb8c   1/1     Running   0          49s

k describe deployment mydeployment
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k describe deployment mydeployment
# Name:                   mydeployment
# Namespace:              default
# CreationTimestamp:      Tue, 22 Feb 2022 23:27:35 -0300
# Labels:                 app=mydeployment
# Annotations:            deployment.kubernetes.io/revision: 1
# Selector:               app=mydeployment
# Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
# StrategyType:           RollingUpdate
# MinReadySeconds:        0
# RollingUpdateStrategy:  25% max unavailable, 25% max surge
# Pod Template:
#   Labels:  app=mydeployment
#   Containers:
#    nginx:
#     Image:        nginx
#     Port:         <none>
#     Host Port:    <none>
#     Environment:  <none>
#     Mounts:       <none>
#   Volumes:        <none>
# Conditions:
#   Type           Status  Reason
#   ----           ------  ------
#   Available      True    MinimumReplicasAvailable
#   Progressing    True    NewReplicaSetAvailable
# OldReplicaSets:  <none>
# NewReplicaSet:   mydeployment-84777db489 (1/1 replicas created)
# Events:
#   Type    Reason             Age   From                   Message
#   ----    ------             ----  ----                   -------
#   Normal  ScalingReplicaSet  2m7s  deployment-controller  Scaled up replica set mydeployment-84777db489 to 1

k get pods
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k get pods
# NAME                            READY   STATUS    RESTARTS   AGE
# mydeployment-84777db489-4cb8c   1/1     Running   0          8m51s

k describe pod mydeployment-84777db489-4cb8c

# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k describe pod mydeployment-84777db489-4cb8c
# Name:         mydeployment-84777db489-4cb8c
# Namespace:    default
# Priority:     0
# Node:         minikube/192.168.49.2
# Start Time:   Tue, 22 Feb 2022 23:27:36 -0300
# Labels:       app=mydeployment
#               pod-template-hash=84777db489
# Annotations:  <none>
# Status:       Running
# IP:           172.17.0.3
# IPs:
#   IP:           172.17.0.3
# Controlled By:  ReplicaSet/mydeployment-84777db489
# Containers:
#   nginx:
#     Container ID:   docker://e707dbcf4cac7da1629b03939746b18812f67d944e3879a0ac3440cf1482d4b4
#     Image:          nginx
#     Image ID:       docker-pullable://nginx@sha256:2834dc507516af02784808c5f48b7cbe38b8ed5d0f4837f16e78d00deb7e7767
#     Port:           <none>
#     Host Port:      <none>
#     State:          Running
#       Started:      Tue, 22 Feb 2022 23:27:47 -0300
#     Ready:          True
#     Restart Count:  0
#     Environment:    <none>
#     Mounts:
#       /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-k85zz (ro)
# Conditions:
#   Type              Status
#   Initialized       True 
#   Ready             True 
#   ContainersReady   True 
#   PodScheduled      True 
# Volumes:
#   kube-api-access-k85zz:
#     Type:                    Projected (a volume that contains injected data from multiple sources)
#     TokenExpirationSeconds:  3607
#     ConfigMapName:           kube-root-ca.crt
#     ConfigMapOptional:       <nil>
#     DownwardAPI:             true
# QoS Class:                   BestEffort
# Node-Selectors:              <none>
# Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
#                              node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
# Events:
#   Type    Reason     Age    From               Message
#   ----    ------     ----   ----               -------
#   Normal  Scheduled  9m16s  default-scheduler  Successfully assigned default/mydeployment-84777db489-4cb8c to minikube
#   Normal  Pulling    9m11s  kubelet            Pulling image "nginx"
#   Normal  Pulled     9m7s   kubelet            Successfully pulled image "nginx" in 3.380093515s
#   Normal  Created    9m5s   kubelet            Created container nginx
#   Normal  Started    9m5s   kubelet            Started container nginx



k scale deployment mydeployment --replicas=5
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k scale deployment mydeployment --replicas=5
# deployment.apps/mydeployment scaled

k get pods
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k get pods
# NAME                            READY   STATUS              RESTARTS   AGE
# mydeployment-84777db489-28zxm   1/1     Running             0          13s
# mydeployment-84777db489-4cb8c   1/1     Running             0          12m
# mydeployment-84777db489-4zgzc   0/1     ContainerCreating   0          13s
# mydeployment-84777db489-nwvnj   0/1     ContainerCreating   0          13s
# mydeployment-84777db489-qh9qp   0/1     ContainerCreating   0          13s

# "ReplicaSet"
# 

k get pods -o wide
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k get pods -o wide
# NAME                            READY   STATUS    RESTARTS   AGE    IP           NODE       NOMINATED NODE   READINESS GATES
# mydeployment-84777db489-28zxm   1/1     Running   0          113s   172.17.0.4   minikube   <none>           <none>
# mydeployment-84777db489-4cb8c   1/1     Running   0          14m    172.17.0.3   minikube   <none>           <none>
# mydeployment-84777db489-4zgzc   1/1     Running   0          113s   172.17.0.5   minikube   <none>           <none>
# mydeployment-84777db489-nwvnj   1/1     Running   0          113s   172.17.0.6   minikube   <none>           <none>
# mydeployment-84777db489-qh9qp   1/1     Running   0          113s   172.17.0.7   minikube   <none>           <none>

# decrease the quantity of pods
k scale deployment mydeployment --replicas=3
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k scale deployment mydeployment --replicas=3
# deployment.apps/mydeployment scaled

k get pods
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k get pods
# NAME                            READY   STATUS    RESTARTS   AGE
# mydeployment-84777db489-4cb8c   1/1     Running   0          16m
# mydeployment-84777db489-nwvnj   1/1     Running   0          3m34s
# mydeployment-84777db489-qh9qp   1/1     Running   0          3m34s

# there are only 3 pods running 

k get pods -o wide
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ k get pods -o wide
# NAME                            READY   STATUS    RESTARTS   AGE   IP           NODE       NOMINATED NODE   READINESS GATES
# mydeployment-84777db489-4cb8c   1/1     Running   0          24h   172.17.0.3   minikube   <none>           <none>
# mydeployment-84777db489-nwvnj   1/1     Running   0          24h   172.17.0.6   minikube   <none>           <none>
# mydeployment-84777db489-qh9qp   1/1     Running   0          24h   172.17.0.7   minikube   <none>           <none>

# https://www.youtube.com/watch?v=d6WC5n9G_sM&t=4020s&ab_channel=freeCodeCamp.org

# try to make a request to one of the pods
curl 172.17.0.6
# it is not successful
# william@william-ThinkPad-T450:~/Documents/statistical-learning$ curl 172.17.0.6
# curl: (7) Failed to connect to 172.17.0.6 port 80: No route to host

# get inside of the minikube cluster and then 
minikube ssh
# [inside the cluster]
curl 172.17.0.6
# this gives the correct response from nginx
# exit the minikube cluster

# [in the main pc]

# Services
# https://youtu.be/d6WC5n9G_sM?t=4167


# next
# https://youtu.be/d6WC5n9G_sM?t=4167



