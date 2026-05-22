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
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKERHUB_USERNAME',
                    passwordVariable: 'DOCKERHUB_PASSWORD'
                )]) {
                    powershell '''
                    $password = $env:DOCKERHUB_PASSWORD
                    $password | docker login -u $env:DOCKERHUB_USERNAME --password-stdin
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