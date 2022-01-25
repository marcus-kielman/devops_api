pipeline {
    agent any 
    stages {
        stage('Setting Up Testing Environment') {
            steps {
                echo 'Pulling Git Stage Branch'
                sh 'git pull origin stage'
            }
            steps{
                sh "echo 'Build API Docker Image and Create Network'"
            }
            steps{
                sh "echo 'Run API and MariaDB Container'"
            }
            steps{
                sh "echo 'Load SQL Database to MariaDB'"
            }
            steps{
                sh "echo 'Run pipenv shell and install requirements'"
            }
        }
        stage('Testing API Docker Image and Network Connection'){
            steps{
                sh "echo 'python api_test.py and check if passed or failed'"
            }
        }
        stage('Push to Production and DockerHub'){
            steps{
                sh "echo 'Stop Docker Containers'"
            }
            steps{
                sh "echo 'Merge Stage to Main and Push Main to GitHub'"
            }
            steps{
                sh "echo 'Merge Main to Develop and Push Develop to GitHub'"
            }
            steps{
                sh "echo 'Push Docker Image API to DockerHub'"
            }
        }
    }
}