pipeline {
    agent any
    stages {
        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Hello World') {
            steps {
                sh "python3 -m pipeline.cli hello"
            }
        }
    }
}
