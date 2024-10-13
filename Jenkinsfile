pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/ShykPavel/playwrightPractice.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('jenkins/jenkins')
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image('jenkins/jenkins').inside {
                        sh 'pip install -r requirements.txt'
                        sh 'pytest tests_ui/'
                    }
                }
            }
        }

        stage('Publish Reports') {
            steps {
            sh 'pytest --template=html1/index.html --report=report.html'
            }
        }
    }

    post {
        always {
            junit '**/report.html'
        }
    }
}
