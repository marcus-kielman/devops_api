pipeline {
    agent any 
    stages {
        stage('Setting Up Testing Environment') {
            steps {
                echo 'Pulling Git Stage Branch'
                sh 'git pull origin stage'
            }
        }
    }
}