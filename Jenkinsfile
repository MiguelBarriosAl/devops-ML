pipeline {
    agent any
        stages {
            stage('Clone Repository'){
                steps {
                    git credentialsId: 'dev_ml', url: 'https://github.com/MiguelBarriosAl/Devops-ML.git'
            }
        }
        stage('Build') {
            steps {
                sh 'sudo apt install python3-pip'
            }
        }
        stage('Testing') {
            steps {
                sh 'python -m test/unittest'
            }
        }
        stage('Build And Push') {
            withCredentials([
                string(
                  credentialsId: 'aws_region',
                  variable: 'AWS_REGION'),
                string(
                  credentialsId: 'ecr_url',
                  variable: 'ECR_URL')
            ]) {
                container('docker') {
                    sh '''
                        echo $AWS_REGION
                        echo $ECR_URL
                        repo_name=$( echo "$repo_name" | tr '[:upper:]'  '[:lower:]' )
                        release_name=$( echo "$repo_name" | tr '_' '-')
                        alias aws='docker run --rm amazon/aws-cli'
                        aws ecr describe-repositories --repository-names ${release_name} || aws ecr create-repository --repository-name ${release_name}
                        aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_URL
                        docker build --cache-from $ECR_URL/${release_name}:latest -t ${release_name}:latest .
                        docker tag ${release_name}:latest $ECR_URL/${release_name}:latest
                        docker push $ECR_URL/${release_name}:latest
                    '''
                }
            }
        }
    }
}
