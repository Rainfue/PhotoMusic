pipeline {
    agent any

    environment {
        TGTOKEN = credentials('tgtoken')
        YMTOKEN = credentials('ymtoken')
        MODEL_PATH = credentials('model_path')
        USER_DB = credentials('users_db')
        TRACKS_DB = credentials('tracks_db')
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
                sh  '''
                    echo "Telegram token: ${TGTOKEN}"
                    echo "Telegram token: ${YMTOKEN}"
                    echo "Telegram token: ${MODEL_PATH}"
                    echo "Telegram token: ${USER_DB}"
                    echo "Telegram token: ${TRACKS_DB}"
                    '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}