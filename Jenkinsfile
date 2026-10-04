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

        stage('Check Docker Credential') {
        steps {
            withCredentials([
                string(
                    credentialsId: 'dockerhub-test2',
                    variable: 'DOCKER_TOKEN'
                )
            ]) {
                powershell '''
                    Write-Host "=============================="
                    Write-Host "Docker Username"
                    Write-Host "=============================="
                    Write-Host "imrandocker3656"

                    Write-Host "=============================="
                    Write-Host "Token Length"
                    Write-Host "=============================="
                    Write-Host $env:DOCKER_TOKEN.Length

                    Write-Host "=============================="
                    Write-Host "Token SHA256"
                    Write-Host "=============================="

                    $bytes = [System.Text.Encoding]::UTF8.GetBytes($env:DOCKER_TOKEN)

                    $hash = [System.Security.Cryptography.SHA256]::Create().ComputeHash($bytes)

                    $hashString = -join ($hash | ForEach-Object {
                        $_.ToString("x2")
                    })

                    Write-Host $hashString
                '''
            }
        }
    }
    
    }
}