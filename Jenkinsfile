pipeline {
    agent any  // Запуск на любом доступном агенте

    stages {
        stage('Hello Jenkins') {
            steps {
                echo '✅ Jenkins работает! Этот шаг выполнен успешно.'
                sh 'echo "Проверка выполнения shell-команды..."'
            }
        }
    }

    post {
        always {
            echo 'Этап "post" всегда выполняется, даже если были ошибки.'
        }
        success {
            echo '🎉 Пайплайн завершился успешно!'
        }
    }
}