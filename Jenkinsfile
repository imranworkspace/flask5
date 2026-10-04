pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\imran\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"
        DOCKER_PATH = "C:\\Users\\imran\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin"
        BACKUP_DIR = "D:/jenkins_backups"

        // DOCKER_IMAGE = "imrandocker3656/flask5"
        // DB_NAME = "fpractice_db2"
        // DB_USER = "postgres"
    }

    stages {

        stage('Check Docker') {
            steps {
                bat '''
                    set "PATH=%DOCKER_PATH%;%PATH%"

                    echo ==============================
                    echo Docker PATH
                    echo ==============================
                    echo %PATH%

                    echo ==============================
                    echo Docker Location
                    echo ==============================
                    where docker

                    echo ==============================
                    echo Docker Version
                    echo ==============================
                    docker --version

                    echo ==============================
                    echo Docker Info
                    echo ==============================
                    docker info

                    if errorlevel 1 (
                        echo Docker Engine is not available
                        exit /b 1
                    )
                '''
            }
        }

        stage('Check Git') {
            steps {
                bat '''
                    echo ==============================
                    echo Git Version
                    echo ==============================
                    git --version

                    echo ==============================
                    echo Git Repository
                    echo ==============================
                    git ls-remote --heads https://github.com/imranworkspace/flask5

                    if errorlevel 1 (
                        echo Git repository check failed
                        exit /b 1
                    )
                '''
            }
        }

        stage('Checkout Code') {
            steps {
                git(
                    branch: 'main',
                    url: 'https://github.com/imranworkspace/flask5'
                )
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat '''
                        set "PATH=%DOCKER_PATH%;%PATH%"

                        echo ==============================
                        echo Docker Executable
                        echo ==============================
                        where docker

                        echo ==============================
                        echo Docker Version
                        echo ==============================
                        docker --version

                        echo ==============================
                        echo Docker User
                        echo ==============================
                        echo %DOCKER_USER%

                        echo ==============================
                        echo Docker Login
                        echo ==============================

                        echo %DOCKER_PASS% | docker login -u "%DOCKER_USER%" --password-stdin

                        if errorlevel 1 (
                            echo ==============================
                            echo Docker login FAILED
                            echo ==============================
                            exit /b 1
                        )

                        echo ==============================
                        echo Docker login SUCCESSFUL
                        echo ==============================
                    '''
                }
            }
        }
    }
}