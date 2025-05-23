pipeline {
    agent any

    post {
        always {
            junit 'report.xml'
        }
        success {
            echo 'Тесты прошли успешно'
        }
        failure {
            echo 'Тест провалились'
        }
    }
}