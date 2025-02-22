pipeline {
    agent { label 'test' }
    environment
    {
        GHCR_USERNAME = 'Nattharika-Jeksungnern'
        GHCR_TOKEN = credentials('ghcr-pat')  // ดึง PAT จาก Jenkins Credentials
        IMAGE_NAME = 'ghcr.io/nattharika-jeksungnern/sample-api'
        IMAGE_TAG = 'jenkins-spdx'
        CONTAINER_NAME = 'sample-api'
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

        stage('Create Container and Map Port')
        {
            steps{
                sh "echo \"jenkins2\" | sudo -S docker stop $CONTAINER_NAME"
                sh "echo \"jenkins2\" | sudo -S docker rm -f sample-api"
                sh "docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME:$IMAGE_TAG" // เป็น bridge network จะใช้ ip เครื่อง VM ที่ run jenkins master
            }
        }

        stage('Clone Robot Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Nattharika-Jeksungnern/sample-api-robot.git'
            }
        }

        stage('Run Robot Tests') {
            steps {
                sh '''#!/bin/bash
                source ./venv/bin/activate && ./venv/bin/python -m robot test-calculate.robot
                '''
            }
        }


        stage('Push sample-api image')
        {
            steps{
                sh "docker push $IMAGE_NAME:$IMAGE_TAG"
            }
        }

    }
}
