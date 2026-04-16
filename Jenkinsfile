pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                sh '''
                rm -rf venv
                python3 -m venv venv
                venv/bin/python -m pip install --upgrade pip
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
            mail to: 'sanjeevan3236@gmail.com',
                 subject: "✅ Build SUCCESS: ${env.JOB_NAME}",
                 body: "Build #${env.BUILD_NUMBER} completed successfully.\nCheck: ${env.BUILD_URL}"
        }

        failure {
            mail to: 'sanjeevan3236@gmail.com',
                 subject: "❌ Build FAILED: ${env.JOB_NAME}",
                 body: "Build #${env.BUILD_NUMBER} failed.\nCheck: ${env.BUILD_URL}"
        }
    }
}
