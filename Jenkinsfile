pipeline {
    agent any 
    stages {
        stage('Setting Up Testing Environment') {
            steps{
                echo 'Pulling Git Stage Branch'
                sh '''
                    git pull origin stage;
                    pip install docker; 
                    ansible-playbook -u jenkins env-playbook.yml -v;
                    docker images ls -a;
                    '''

                sh "echo 'Build API Docker Image and Create Network'"
                sh "echo 'Run API and MariaDB Container'"
                sh "echo 'Load SQL Database to MariaDB'"
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
                sh "echo 'Merge Stage to Main and Push Main to GitHub'"
                sh "echo 'Merge Main to Develop and Push Develop to GitHub'"
                sh "echo 'Push Docker Image API to DockerHub'"
            }
        }
    }
}