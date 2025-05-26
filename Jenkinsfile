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
                    echo "YaMusic token: ${YMTOKEN}"
                    echo "Classifiction model path: ${MODEL_PATH}"
                    echo "User database path: ${USER_DB}"
                    echo "Tracks database path: ${TRACKS_DB}"
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