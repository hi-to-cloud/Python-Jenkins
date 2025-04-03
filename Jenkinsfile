pipeline {
    agent any
    environment {
        PYTHONPATH = "$WORKSPACE/src"
    }
    stages {
        stage('Clone Python Shared Library') {
            steps {
                    sh '''
                        if [ -d "shared-lib" ]; then rm -rf shared-lib; fi
                        git clone https://github.com/hi-to-cloud/Python-Jenkins.git shared-lib
                        cd shared-lib && ls -al && python3 -m venv venv && . venv/bin/activate && pwd && ls -al && pip install -r requirements.txt
                    '''
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
