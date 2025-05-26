pipeline {
    agent any
    stages {
        stage('Load .env') {
            steps {
                script {
                    def envVars = readFile('.env').split('\n')
                    withEnv(envVars) {
                        sh 'echo "TGTOKEN is $TGTOKEN"'
                    }
                }
            }
        }
        stage('Build') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
        stage('Tests') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}