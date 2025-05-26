pipeline {
    agent any

    environment {
        TGTOKEN = credentials('tgtoken')
        YMTOKEN = credentials('ymtoken')
        MODEL_PATH = credentials('model_path')
        USER_DB = credentials('users_db')
        TRACKS_DB = credentials('tracks_db')
        VENV_DIR = '.venv'
    }

    stages {
        stage('Logs') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                sh 'docker --version'
                // Проверяем, какой Python доступен
                sh '''
                    echo "Available Python versions:"
                    which python || true
                    which python3 || true
                    python --version || python3 --version || echo "Python not found"
                '''
            }
        }

        stage('Setup Python') {
            steps {
                // Вместо установки через apt - используем готовый Python
                sh '''
                    python3 -m ensurepip --upgrade
                    python3 -m pip install --upgrade pip
                    python3 --version
                '''
            }
        }

        stage('Vars') {
            steps {
                echo 'Get vars...'
                sh '''
                    echo "Telegram token: ${TGTOKEN}"
                    echo "YaMusic token: ${YMTOKEN}"
                    echo "Model path: ${MODEL_PATH}"
                    echo "User DB path: ${USER_DB}"
                    echo "Tracks DB path: ${TRACKS_DB}"
                '''
            }
        }

        stage('Prepare venv') {
            steps {
                echo 'Creating venv...'
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    python -m pytest tests/
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}