pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\imran\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"
        // DOCKER_IMAGE = "imrandocker3656/flask5"
        // DB_NAME = "fpractice_db2"
        // DB_USER = "postgres"
        BACKUP_DIR = "D:/jenkins_backups"
    }

    stages {

        stage('Check Docker') {
            steps {
                bat '''
                    set "PATH=C:\\Users\\imran\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;%PATH%"

                    echo ===== Docker PATH =====
                    echo %PATH%

                    echo ===== Docker Location =====
                    where docker

                    echo ===== Docker Version =====
                    docker --version

                    echo ===== Docker Info =====
                    docker info


                '''
            }
        }

        stage('Check Git') {
            steps {
                bat '''
                    git ls-remote --heads https://github.com/imranworkspace/flask5
                    
                '''
            }
        }
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/imranworkspace/flask5'
            }
        }

        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-credentials',
            usernameVariable: 'DOCKER_USER',
            passwordVariable: 'DOCKER_PASS'
        )]) {
            bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
        }

    }
}

