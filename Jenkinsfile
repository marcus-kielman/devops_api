pipeline {
    agent any 
    stages {
        stage('Setting Up Testing Environment') {
            steps{
                sh '''
                    echo "Pulling Git Stage Branch"
                    git pull origin stage
                    pip install docker
                    pip install -- update wheel
                    pip install -- update setuptools
                    pip install -r requirements.txt
                    ansible-playbook -u jenkins env-playbook.yml -v
                    docker start mariadb || exit 1
                    docker run -p 8081:8081 --network api_maria --name devops_api marcuskielman/devops_api &
                    '''
            }
        }
        stage('Testing API Docker Image and Network Connection'){
            steps{
                sh "echo 'python api_test.py and check if passed or failed'"
                sh 'python api_test.py || docker container stop devops_api mariadb && docker container rm devops_api'
                sh 'docker container stop devops_api mariadb'
                sh 'docker container rm devops_api'
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