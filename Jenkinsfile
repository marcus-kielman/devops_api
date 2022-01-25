pipeline {
    agent any 
    stages {
        stage('Setting Up Testing Environment') {
            steps {
                echo 'Pulling Git Stage Branch'
                sh 'git pull origin stage'
            }
            steps{
                echo 'Build API Docker Image and Create Network'
            }
            steps{
                echo 'Run API and MariaDB Container'
            }
            steps{
                echo 'Load SQL Database to MariaDB'
            }
            steps{
                echo 'Run pipenv shell and install requirements'
            }
        }
        stage('Testing API Docker Image and Network Connection'){
            steps{
                echo 'python api_test.py and check if passed or failed'
            }
        }
        production('Push to Production and DockerHub'){
            steps{
                echo 'Stop Docker Containers'
            }
            steps{
                echo 'Merge Stage to Main and Push Main to GitHub'
            }
            steps{
                echo 'Merge Main to Develop and Push Develop to GitHub'
            }
            steps{
                echo 'Push Docker Image API to DockerHub'
            }
        }
    }
}