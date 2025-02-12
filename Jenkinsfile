pipeline {
    agent { label 'vm2' }

    stages {
        stage('Clone API Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Nattharika-Jeksungnern/sample-api.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install --upgrade pip'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
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
