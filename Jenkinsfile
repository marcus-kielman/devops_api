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
                sh '''echo "python api_test.py and check if passed or failed"
                    python api_test.py
                    docker container stop devops_api mariadb && docker container rm devops_api
                '''
            }
        }
        stage('Push to Production and DockerHub'){
            steps{
                sh '''
                    echo 'Merge stage to main, main to deveop, and push main and develop to GitHub'
                    git checkout main
                    git merge stage
                    git checkout develop
                    git merge main
                '''
                sh "echo 'Push Docker Image API to DockerHub'"
            }
        }
    }
}