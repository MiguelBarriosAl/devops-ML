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
                    sh 'pip install -r requirements.txt'
            }
        }

    }
}
