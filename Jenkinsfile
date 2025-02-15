pipeline {
    agent { label 'vm2' }
    environment
    {
        GHCR_USERNAME = 'Nattharika-Jensungnern'
        GHCR_TOKEN = credentials('ghcr-pat')  // ดึง PAT จาก Jenkins Credentials
        IMAGE_NAME = 'ghcr.io/nattharika-jensungnern/sample-api'
        IMAGE_TAG = 'jenkins-spdx'
    }

    stages {
        stage('Clone API Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Nattharika-Jeksungnern/sample-api.git'
            }
        }

        // ไปที่ VM ตาม agent แล้วลง python venv, flask ใน folder pipline นั้น ใช้ state แล้วไม่ได้

        stage('Run Unit Tests') {
            steps {
                sh './venv/bin/python -m unittest discover -s tests'
            }
        }

        stage('Login to GHCR') {
            steps {
                withCredentials([string(credentialsId: 'ghcr-pat', variable: 'GHCR_TOKEN')]) {
                sh 'echo "$GHCR_TOKEN" | docker login ghcr.io -u your-github-username --password-stdin'
                }

            }

        }

        stage('Build and Push Image') {
            steps {
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
                sh "docker push $IMAGE_NAME:$IMAGE_TAG"
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
