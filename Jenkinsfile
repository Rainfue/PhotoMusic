pipeline {
    agent any
    
    stages {
        stage('Check OS') {
            steps {
                script {
                    // Проверка типа ОС
                    def isUnix = isUnix()
                    echo "Running on Unix-like system: ${isUnix}"
                    
                    // Детальная информация об ОС
                    if (isUnix) {
                        sh '''
                            echo "System Info:"
                            uname -a
                            echo "Linux Distro:"
                            lsb_release -a || cat /etc/*release || echo "No distro info available"
                        '''
                    } else {
                        bat '''
                            echo "Windows System Info:"
                            ver
                            systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
                        '''
                    }
                }
            }
        }
    }
}