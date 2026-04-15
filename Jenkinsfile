pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/sanjeev2907/myapp.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3.12 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
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
}
