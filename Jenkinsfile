pipeline {
    agent any 
    environment{
        DOCKERHUB_CREDENTIALS = credentials('58a5093f-254a-4b81-97c6-b2e2c3c0b481')
    }
    stages {
        stage('Setting Up Testing Environment') {
            steps{
                sh '''
                    echo "Pulling Git Stage Branch and Installing Dependencies"
                    git pull origin stage
                    ansible-playbook -u jenkins env-playbook.yml -v
                    docker start mariadb || exit 0
                    docker run -p 8081:8081 -h devops_api --network api_maria --name devops_api marcuskielman/devops_api &
                    '''
            }
        }
        stage('Testing API Docker Image and Network Connection'){
            steps{
                sh 'curl http://172.18.0.3:8081 && exit 0'
                sh '''echo "python api_test.py and check if passed or failed"
                    sleep 10s
                    python test_files/api_test.py
                    docker container stop devops_api mariadb && docker container rm devops_api
                '''
            }
        }
        stage('Push to Production and DockerHub'){
            steps{
                sh '''
                    echo 'Push Docker API Image to DockerHub'
                    echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    docker push marcuskielman/devops_api:latest
                '''
            }
        }
    }
}