# DevOps Case Study v0.0.6
## DevOps Developed API

This repository runs an API that communicates with a MariaDB database, applies a CI/CD approach to testing and version control, and IaC an for deployment.

## Features

- Send GET requests to retrieve the database table, payments table, customers table, and offices table
- Send POST requests to insert a new row into the customers table and payments table


## Requirements for compatibility

The API requires Python 3.9 for API functionality. The following libraries needed can be found in the requirements.txt file and npm 7.13.0+, along with Python 3.8 and pip 20.0.2, and the following libraries for both Node.js, and Python 3.8 in your virtual environment

| Python                  
| ------                  
| certifi==2021.10.8
| charset-normalizer==2.0.10
| click==8.0.3
| flake8==4.0.1
| Flask==2.0.2
| greenlet==1.1.2
| idna==3.3
| itsdangerous==2.0.1
| Jinja2==3.0.3
| mariadb==1.0.9
| MarkupSafe==2.0.1
| marshmallow==3.14.1
| mccabe==0.6.1
| pycodestyle==2.8.0
| pyflakes==2.4.0
| requests==2.27.1
| urllib3==1.26.8
| Werkzeug==2.0.2        

At the time of development, this API is compatible with any Linux distribution.
Python libraries can be installed using the command

```
pip install -r requirements.txt
```

## Environment Setup

For Development, a Pipfile has been provided for utilizing pipenv. You can access
this environment using the command ```$ pipenv shell```

Docker is used to containerize the API and MariaDB Database independently. Docker 
containers can be created using the following commands:
```
$ cd devops_api
$ docker build -t marcuskielman/devops_api .    # Builds API image
$ docker network create api_mariadb             # Creates shared network for API and Database
$ docker run -p 3306:3306 -h mariadb --network api_mariadb --name mariadb -d marcuskielman/mariadb    # Pulls marcuskielman/mariadb from DockerHub and runs container
$ docker run -p 8081:8081 -h devops_api --network api_maria --name devops_api marcuskielman/devops_api    # Runs API as container
$ docker exec -i mariadb mysql -uroot -proot classicmodels < mysqlsampledatabase.sql    # Imports mysqlsampledatabase.sql to database
```

For CI/CD Setup and Testing, Jenkins is utilized and deployed at port 8080 for creating a Pipeline from the GitHub repository to the Jenkins server. The Jenkinsfile in the repository pulls from this repository, builds the API image, and sets up the development environment for testing. API image builds will be sent to DockerHub and Kubernetes/Minikube on successful testing.

## Interface Controls
The main interface for the application is the ```curl``` command in Linux. This can be installed using ```sudo apt install curl```. 
The following urls are used to send GET and POST requests to the API Docker Containers:

        http://localhost:8081  ----------------------------------> GET main page to API
        http://localhost:8081/get_database_table ----------------> GET all database table rows
        http://localhost:8081/get_database_table/customers ------> GET all customers table rows and POST new row
        http://localhost:8081/get_database_table/payments -------> GET all payments table rows and POST new row
        http://localhost:8081/get_database_table/offices --------> GET all offices table rows

## Application Architecture
### Project Folder Structure

```bash
├── devops_api
│   ├── api
|   |   ├── model
|   |   |   ├── customers.py
|   |   |   ├── offices.py
|   |   |   ├── payments.py
|   |   |   └── tables.py
│   │   └── mxk_api.py
│   ├── kube_files
|   |   ├── api_kube.yml
|   |   ├── api_maria_kube.yml
│   ├── test_files
|   |   ├── api_test.py
|   |   ├── kube_test.py
|   |   ├── kube-run.sh
|   |   ├── del-docker-entries.sh
|   |   └── del-test-entries.sh
|   |
│   ├── Dockerfile
│   ├── Jenkinsfile
│   ├── mysqlsampledatabase.sql
│   ├── Pipfile
│   ├── requirements.txt
│   ├── env-playbook.yml
│   ├── kube-playbook.yml
│   └── README.md

```

## Testing
The following Python files have been created as unit tests for Docker containers (```api_test.py```) and Kubernetes pods (```kube_test.py```). ```api_test.py``` can also be used as general unit testing during development. Both can be run using the command ```python3 kube_test.py``` or alternatively ```python3 api_test.py```

### Testing Cleanup
The following shell scripts ```del-docker-entries.sh``` and ```del-test-entries.sh``` are used to remove rows in the database added for testing the docker containers and kubernetes pods respectively. They can be run as executable files through the terminal.

## Ansible Environment Setup and Deployment
There are two playbooks used for creating the testing environment, and deploying to kubernetes. When running CI/CD testing in Jenkins, the ```env-playbook.yml``` playbook is used to install necessary packages and libraries for testing docker container functionality and Python linting testing. On success, the ```kube-playbook.yml``` playbook is used to determine if pods are already created or not, and deploy accordingly. 

### Deployment
Additional running for deployment can be accomplished using the ```test_files/kube-run.sh``` to enable port forwarding and run unit testing on kubernetes pods. Two types of .yml files are provided for deploying the API and database (```api_maria_kube.yml```) and deploying only the API (```api_kube.yml```). In cases where the API and database haven't been deployed, deployment occurs using the command ```kubectl apply -f kube_files/api_maria_kube.yml```. In cases where the database is running and persistence should remain, updating the API occurs using the command ```kubectl replace -f kube_files/api_kube.yml```