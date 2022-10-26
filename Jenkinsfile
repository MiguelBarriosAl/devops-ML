pipeline {
    agent any
        stages {
            stage('Clone Repository'){
                steps {
                    git credentialsId: 'dev_ml', url: 'https://github.com/MiguelBarriosAl/Devops-ML.git'
            }
        }
        stage('Testing') {
            steps {
                sh 'python -m unittest test/test_model_deployed.py'
                sh 'python -m unittest test/test_heathcheck_api.py'
            }
        }
        stage('Build Image'){
             steps  {
                    sh 'sudo docker build -t tensor-prediction:v1 .'
            }
        }
    }
}
