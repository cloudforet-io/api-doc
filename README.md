# Quickstart Guide of Cloudforet API Documentation

This guide covers how you can quickly get started using various tools to access Cloudforest's API Documentation which auto-generated from [API's Protobuffs](https://github.com/cloudforet-io/api)

---
# Prerequisites
- [Hugo](https://gohugo.io/getting-started/installing/) 
- [Docker](https://docs.docker.com/get-docker/)
- [Kubernetes](https://kubernetes.io/docs/tasks/tools/install-kubectl/) or [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) 



This repository can be deployed 
- as Github Pages
- as Docker Image
- as Kubernetes Pod using Helm Chart
- as Hugo Server

---

# Deploying as Github Pages
[Fork](https://github.com/cloudforet-io/api-doc/fork) this repository and execute `[PUSH] Deploy Hugo to GitHub Pages` Github Actions to deploy as Github Pages.


---

# Deploying as Docker Image
Execute following command to run as Docker Image

1. Run Docker Image
   ```
   docker run -p 1313:1313 cloudforet/api-doc:{version}
   ```
---

# Deploying as Kubernetes Pod using Helm Chart(Not yet supported)
Execute following command to run as Kubernetes Pod using Helm Chart

1. Add Helm Repository
    ```
    helm repo add cloudforet https://cloudforet-io.github.io/api-doc/deploy/helm
    ```
   
2. Create Namespace
    ```
    kubectl create namespace api-docs
    ```

3. Install Helm Chart
    ```
    helm install api-docs cloudforet/cloudforet-api-docs
    ```
   
---

# Deploying as Hugo Server
Execute following command to run as Hugo Server

1. Clone this repository
    ```
    git clone https://cloudforet-io.github.io/api-doc.git
    ```

2. Update Submodule
    ```
    git submodule update --init --recursive
    ```
   
3. Run Hugo Server
    ```
    hugo server --gc --minify --theme hugo-book --baseUrl="http://localhost:1313"
    ```