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
                    powershell '''
                        $env:Path = "$env:DOCKER_PATH;$env:Path"

                        Write-Host "=============================="
                        Write-Host "Docker User"
                        Write-Host "=============================="
                        Write-Host $env:DOCKER_USER

                        Write-Host "=============================="
                        Write-Host "Docker Version"
                        Write-Host "=============================="
                        docker --version

                        Write-Host "=============================="
                        Write-Host "Token Length"
                        Write-Host "=============================="
                        Write-Host $env:DOCKER_PASS.Length

                        Write-Host "=============================="
                        Write-Host "Docker Login"
                        Write-Host "=============================="

                        $env:DOCKER_PASS | docker login `
                            --username $env:DOCKER_USER `
                            --password-stdin

                        if ($LASTEXITCODE -ne 0) {
                            Write-Host "Docker login FAILED"
                            exit 1
                        }

                        Write-Host "Docker login SUCCESSFUL"
                    '''
                }
            }
        }
    }
}