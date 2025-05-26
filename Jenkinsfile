pipeline {
    agent any

    environment {
        TGTOKEN = credentials('TGTOKEN')
    }

    stages {
        stage('Build') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
        stage('Tests') {
            steps {
                echo 'Testing...'
                steps {
                    bat 'echo %TGTOKEN%' 
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}