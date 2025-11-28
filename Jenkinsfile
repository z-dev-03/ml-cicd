pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Build & Test') {
            steps {
                bat 'python ml_pipeline.py'
            }
        }
        stage('Deploy') {
            steps {
                bat 'python deploy.py'
            }
        }
    }
    post {
        success { 
            echo ' CI/CD SUCCESS - Model Deployed' 
        }
        failure { 
            echo ' CI/CD FAILED' 
        }
    }
}
