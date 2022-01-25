pipeline {
    agent any 
    stages {
        stage('Setting Up Testing Environment') {
            steps('Pulling Git Stage Branch'){
                echo 'Pulling Git Stage Branch'
                sh 'git pull origin stage'
            }
            steps('Build API Docker Image and Create Network'){
                sh "echo 'Build API Docker Image and Create Network'"
            }
            steps('Run API and MariaDB Container'){
                sh "echo 'Run API and MariaDB Container'"
            }
            steps('Load SQL Database to MariaDB'){
                sh "echo 'Load SQL Database to MariaDB'"
            }
            steps('Run pipenv shell and install requirements'){
                sh "echo 'Run pipenv shell and install requirements'"
            }
        }
        stage('Testing API Docker Image and Network Connection'){
            steps{
                sh "echo 'python api_test.py and check if passed or failed'"
            }
        }
        stage('Push to Production and DockerHub'){
            steps('Stop Docker Containers'){
                sh "echo 'Stop Docker Containers'"
            }
            steps('Merge stage to main and push main'){
                sh "echo 'Merge Stage to Main and Push Main to GitHub'"
            }
            steps('merge main to develop and push develop'){
                sh "echo 'Merge Main to Develop and Push Develop to GitHub'"
            }
            steps('push docker image API to DockerHub'){
                sh "echo 'Push Docker Image API to DockerHub'"
            }
        }
    }
}