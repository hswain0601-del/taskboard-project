pipeline {
    agent any

    environment {
        IMAGE_NAME = "himansh0074/taskboard-app-project"
        IMAGE_TAG  = "v1"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Login to Docker Hub') {
    steps {
        withCredentials([string(
            credentialsId: 'dockerhub-token',
            variable: 'DOCKER_TOKEN'
        )]) {

            powershell '''
            $env:DOCKER_TOKEN | docker login -u himansh0074 --password-stdin
            '''

        }
    }
}

        stage('Push Docker Image') {
            steps {
                bat "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }
    }
}