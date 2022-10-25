pipeline {
    agent any
        stages {
            stage('Clone Repository'){
                steps {
                    git credentialsId: 'dev_ml', url: 'https://github.com/MiguelBarriosAl/Devops-ML.git'
            }
        }
         stage('Build'){
             steps {
                    sh '''
                        docker build -t tensor-prediction .
                        docker run -p 80:80 tensor-prediction
                       '''
            }
        }

    }
}
