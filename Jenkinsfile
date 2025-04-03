pipeline {
    agent any
    environment {
        PYTHONPATH = "$WORKSPACE/src"
    }
    stages {
        stage('Clone Python Shared Library') {
            steps {
                sh 'git clone https://github.com/my-org/python-jenkins-shared-lib.git shared-lib'
                sh 'cd shared-lib && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                sh "python3 shared-lib/src/pipeline/cli.py build"
            }
        }
        stage('Deploy') {
            steps {
                sh "python3 shared-lib/src/pipeline/cli.py deploy --env production"
            }
        }
    }
}
