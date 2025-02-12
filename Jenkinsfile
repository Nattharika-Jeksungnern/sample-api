pipeline {
    agent { label 'vm2' }

    stages {
        stage('Clone API Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Nattharika-Jeksungnern/sample-api.git'
            }
        }

        stage('Debug Environment') {
            steps {
                sh 'echo "Python Path: $(which python3)"'
                sh 'python3 --version'
                sh 'python3 -m site'
                sh 'python3 -m pip list'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/python -m pip install --upgrade pip'
                sh './venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Check Python') {
            steps {
                sh 'which python3'
                sh 'python3 --version'
                sh 'python3 -m site'
            }
        }

        stage('Verify Flask Installation') {
            steps {
                sh './venv/bin/python -m pip list | grep Flask'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest discover -s tests'
            }
        }

        // stage('Build & Push Docker Image') {
        //     steps {
        //         sh 'docker build -t your-registry/simple-api:latest .'
        //         sh 'docker push your-registry/simple-api:latest'
        //     }
        // }

        // stage('Trigger Pre-Prod Deployment') {
        //     steps {
        //         build job: 'VM3_PreProd_Pipeline'  // เรียก Pipeline ของ VM 3
        //     }
        // }
    }
}
