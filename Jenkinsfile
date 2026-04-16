pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                chmod -R 755 venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                pkill gunicorn || true
                . venv/bin/activate
                nohup gunicorn app:app --bind 0.0.0.0:8000 &
                '''
            }
        }
    }
}
