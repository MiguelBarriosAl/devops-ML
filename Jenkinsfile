pipeline {
    agent {
            docker { image 'python:3.9-buster' }
        }
        stages {
            stage('Clone Repository'){
                steps {
                    git credentialsId: 'dev_ml', url: 'https://github.com/MiguelBarriosAl/Devops-ML.git'
            }
        }
         stage('Run Test'){
             steps {
                    sh '''
                        python -m pip install -r requirements.txt
                       '''
            }
        }

    }
}
