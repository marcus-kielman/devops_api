pipeline {
    agent any 
    stages {
        stage('Setting Up Testing Environment') {
            steps{
                sh '''
                    echo "Pulling Git Stage Branch"
                    git pull origin stage
                    docker run -p 3306:3306 --network api_maria --name maria_db -v data:/data -e MYSQL_DATABASE=classicmodels -e MYSQL_ROOT_PASSWORD=root -d marcuskielman/mariadb
                    docker run -p 8081:8081 --network api_maria --name devops_api marcuskielman/devops_api &
                    '''
            }
        }
        stage('Testing API Docker Image and Network Connection'){
            steps{
                sh "echo 'python api_test.py and check if passed or failed'"
                sh "curl http://172.18.0.3:8081 || docker container stop devops_api maria_db && docker container rm devops_api maria_db"
                sh 'python api_test.py || docker container stop devops_api maria_db && docker container rm devops_api maria_db '
                sh 'docker container stop devops_api maria_db'
                sh 'docker container rm devops_api maria_db'
            }
        }
        stage('Push to Production and DockerHub'){
            steps{
                sh "echo 'Merge Stage to Main and Push Main to GitHub'"
                sh "echo 'Merge Main to Develop and Push Develop to GitHub'"
                sh "echo 'Push Docker Image API to DockerHub'"
            }
        }
    }
}