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

        stage('Prepare Docker Config and Login') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKER_TOKEN')]) {
                    powershell '''
                    $ErrorActionPreference = "Stop"
                    $env:DOCKER_CONFIG = "$env:WORKSPACE\\.docker-config"
                    New-Item -ItemType Directory -Force $env:DOCKER_CONFIG | Out-Null
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