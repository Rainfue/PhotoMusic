pipeline {
    // Использование агента с python из docker образа
    agent any

    // Получаем secrets
    environment {
        // API-ключи
        TGTOKEN = credentials('tgtoken')
        YMTOKEN = credentials('ymtoken')
        // Пути
        MODEL_PATH = credentials('model_path')
        USER_DB = credentials('users_db')
        TRACKS_DB = credentials('tracks_db')
        // Имя venv
        VENV_DIR = '.venv'
    }

    stages {
        // Логирование
        stage('Logs') {
            steps {
                // Номер сборки и ссылка на запущенный Jenkins
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                // Проверяю верию docker
                sh  '''
                    docker --version
                    '''
            }
        }

        // Установка python
        stage('Check Python') {
            steps {
                sh  '''
                    python3 --version
                    '''
            }
        }

        
        // Проверка путей и API-ключей (переменных)
        stage('Vars') {
            steps {
                echo 'Get vars...'
                sh  '''
                    echo "Telegram token: ${TGTOKEN}"
                    echo "YaMusic token: ${YMTOKEN}"
                    echo "Classifiction model path: ${MODEL_PATH}"
                    echo "User database path: ${USER_DB}"
                    echo "Tracks database path: ${TRACKS_DB}"
                    echo "Venv name: ${VENV_DIR}"
                    '''
            }
        }

        // Подготовка виртуального окружения
        stage('Prepare venv') {
            steps {
                echo 'Starting create venv...'
                // Создаю виртуальное окружение
                sh  '''
                    python3 -m venv $VENV_DIR
                    . ${VENV_DIR}/bin/activate || . ${VENV_DIR}/bin/activate.sh
                    which python
                    pip install pandas
                    '''
                    // ${VENV_DIR}/bin/pip install pandas
            }
        }

        // Unit-тесты
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