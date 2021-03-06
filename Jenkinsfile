pipeline {
    agent any 
    environment{
        DOCKERHUB_CREDENTIALS = credentials('1f52453e-8550-4791-9780-43ec470acfdb')
    }
    stages {
        stage('Setting Up Testing Environment') {
            steps{
                sh '''
                    echo "Pulling Git Stage Branch and Installing Dependencies"
                    git pull origin main
                    ansible-playbook -u jenkins env-playbook.yml -v
                    '''
            }
        }
        stage('Test Styling for Python Files'){
            steps{
                sh '''
                    flake8 api/model/customers.py
                    flake8 api/model/offices.py
                    flake8 api/model/payments.py
                    flake8 api/model/tables.py
                    flake8 api/mxk_api.py
                    flake8 test_files/api_test.py
                    flake8 test_files/kube_test.py
                '''
            }
        }
        stage('Testing API Docker Image and Network Connection'){
            steps{
                sh '''
                    echo "python api_test.py and check if passed or failed"
                    docker build -t marcuskielman/devops_api .
                    docker pull marcuskielman/mariadb
                    docker network create api_maria
                    docker run -p 8081:8081 -h devops_api --network api_maria --name devops_api marcuskielman/devops_api &
                    docker run -p 3306:3306 -h mariadb --network api_maria --name mariadb  -d marcuskielman/mariadb
                    sleep 160s
                    docker exec -i mariadb mysql -uroot -proot classicmodels < mysqlsampledatabase.sql
                '''
                script{
                    try{
                        sh '''
                            curl http://192.168.1.245:8081
                            curl http://192.168.1.245:8081/get_database_table
                            curl http://192.168.1.245:8081/get_database_table/payments
                            curl http://192.168.1.245:8081/get_database_table/customers
                            python3 test_files/api_test.py
                            docker container stop devops_api mariadb && docker container rm devops_api mariadb
                            docker image rm marcuskielman/mariadb
                        '''
                    }
                    catch(error){
                        sh '''
                            docker container stop devops_api mariadb && docker container rm devops_api mariadb
                            docker image rm marcuskielman/devops_api marcuskielman/mariadb
                        '''

                    }
                }
            }
        }
        stage('Push to Production and DockerHub'){
            steps{
                sh '''
                    echo 'Push Docker API Image to DockerHub'
                    echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    docker push marcuskielman/devops_api:latest
                    docker image rm marcuskielman/devops_api
                '''
            }
        }
        stage('Deploy to Kubernetes'){
            steps{
                sshagent(credentials:['605e4d7e-ed8b-4069-932d-0fac12d41de1']){
                    sh "ssh -o StrictHostKeyChecking=no userver1@192.168.1.245 cd /home/userver1/devops_api && git pull origin main"
                    sh "ssh -o StrictHostKeyChecking=no userver1@192.168.1.245 ansible-playbook /home/userver1/devops_api/kube-playbook.yml -v"
                }
            }
        }
    }
}
