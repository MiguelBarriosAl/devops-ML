<h1 align="center"> Deploy ML models with FastAPI, Docker, and CI/CD </h1>

# Table of Contents

- [Introduction](#Introduction)
- [Requirements](#Requirements)
- [Services](#Services)
# Introduction

The aim of this project is to simulate an architecture for automated production deployment of a pytorch pre-trainer model. The service allows the client to query the predictions of the pre-trained model through an array.
This model returns a 1-dim tensor multiplied by 2.
# Requirements
- Service:

  - fastapi==0.85.1
  - torch==1.12.1
  - numpy==1.23.4
  - requests==2.28.1
  - starlette==0.20.4
  
- CI/CD:

  - Jenkins

- PaaS:
  - Heroku==7.65.0

- IaC:
  - Terraform==1.3.3

# Create Git repo
    sudo su    
    visudo -f /etc/sudoers

# Services
###**HealthCheck**

    curl -X 'GET' \
      'https://devops-ml-dev.herokuapp.com/' \
      -H 'accept: application/json'


- Response body

`    {
      "HealthCheck": "Ok",
      "Version": "0.1.0"
    }`

###**Predict**

    curl -X 'POST' \
      'https://devops-ml-dev.herokuapp.com/predict' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "tensor": [
        0,1,2
      ]
    }'


- Response body

`"{"tensor": [0, 2, 4]}"`

###**Document FastApi**

`https://devops-ml-dev.herokuapp.com/docs`


# Comments
For this project, we wanted to carry out a simple automation in which unit tests are simply executed.
In a real production environment, after performing some unit tests it would be interesting to make a deployment in production as it could be in a cloud service server by adding the following code in jenkinsfile. 

For the following projects, it is important to deploy in a scalable and fault-tolerant way. To do so, I would consider the possibility for production to make an architecture where the client only makes requests to FastApi services, and FastApi requests predictions to a Docker Compose model.
  Docker Compose integrated into Kubernetes or Docker Swarm scales the number of models depending on the resources available to the requests.
  Docker Swarm has logs that can be integrated with Prometheus and Grafana for monitoring resources such as RAM or CPU required by models. 


