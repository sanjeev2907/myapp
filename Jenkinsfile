 pipeline {
    agent any

    environment {
        APP_PORT = "8000"
    }

    stages {

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/sanjeev2907/myapp.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                venv/bin/pip install --upgrade pip
                venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                echo "Running basic test..."
                venv/bin/python -m py_compile app.py
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                echo "Starting application..."
                pkill -f gunicorn || true
                nohup venv/bin/gunicorn app:app --bind 0.0.0.0:$APP_PORT &
                '''
            }
        }
    }

    post {
        success {
            mail to: 'yourmail@gmail.com',
                 subject: "✅ Build Success",
                 body: "Jenkins pipeline executed successfully."
        }
        failure {
            mail to: 'yourmail@gmail.com',
                 subject: "❌ Build Failed",
                 body: "Jenkins pipeline failed. Please check logs."
        }
    }
}
