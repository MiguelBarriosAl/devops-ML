pipeline {
    agent any
        stages {
            stage('Clone Repository'){
                steps {
                    git credentialsId: 'dev_ml', url: 'https://github.com/MiguelBarriosAl/Devops-ML.git'
            }
        }
         stage('Run Test'){
             steps {
                    sh '''
                        pip install -r requirements.txt
                        python -m unittest test/test_model_deployed.py
                        python -m unittest test/test_heathcheck_api.py
                       '''
            }
        }

    }
}
