pipeline {
    agent { docker { image 'python:3.9' } }
    stages {
        stage('Clone Repository'){
            steps {
                git credentialsId: 'dev_ml', url: 'https://github.com/MiguelBarriosAl/Devops-ML.git'
            }
        }
        stage('Run and Test'){
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'pip install -r requirements.txt'
                sh 'python -m unittest '
                }
            }
        }
    }
}