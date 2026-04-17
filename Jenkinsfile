pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/sanjeev2907/myapp.git'
            }
        }

        stage('Setup') {
            steps {
                sh '''
                python3 -m venv venv
                venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                pkill gunicorn || true
                nohup venv/bin/gunicorn app:app --bind 0.0.0.0:8000 &
                '''
            }
        }
    }
post {
    success {
        echo 'Build successful'
    }
    failure {
        echo 'Build failed'
    }
}
