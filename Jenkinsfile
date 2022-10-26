pipeline {
    agent any
        stages {
            stage('Clone Repository'){
                steps {
                    git credentialsId: 'dev_ml', url: 'https://github.com/MiguelBarriosAl/Devops-ML.git'
            }
        }
         stage('Build Image'){
             steps  {
                    sh 'docker build -t tensor-prediction:v1 .'
            }
        }
        stage('Run Image') {
            steps {
                    sh 'docker run -p 80:80 tensor-prediction'
            }
        }
        stage('Testing') {
            steps {
                echo 'Testing....'
            }
        }
    }
}
