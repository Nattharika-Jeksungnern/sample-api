pipeline {
    agent { label 'vm2' }
    environment
    {
        GHCR_USERNAME = 'Nattharika-Jeksungnern'
        GHCR_TOKEN = credentials('ghcr-pat')  // ดึง PAT จาก Jenkins Credentials
        IMAGE_NAME = 'ghcr.io/nattharika-jeksungnern/sample-api'
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

        stage('Build Image') {
            steps {
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
            }
        }

        stage('Create Container')
        {
            steps{
                sh "docker run -d --name $CONTAINER_NAME $IMAGE_NAME:$IMAGE_TAG"
            }
        }

        // step('Push sample-api image')
        // {
        //     steps{
        //         sh "docker push $IMAGE_NAME:$IMAGE_TAG"
        //     }
        // }

    }
}
