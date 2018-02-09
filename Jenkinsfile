pipeline {
    agent any

    stages {

        stage('get_latest_version') {
            steps {
                deleteDir()
                git branch: 'master', credentialsId: '5fad5bee-c7dd-4776-b766-9db845450257', url: 'https://github.com/dominikatrela/poc_flask_docker/'
            }
        }
        stage('application_up') {
            steps {
                sh 'docker --version'
                sh 'docker-compose down'
                sh 'docker-compose up -d'

            }
        }
        stage('check_if_page_is_up') {
            steps {
                sh 'make run-test-for-checking-if-page-is-up'

            }
        }

        stage('test_run_page') {
            steps {
                sh 'make run-test-hits'

            }
        }

	stage('test_gui') {
            steps {
                sh 'first_test.py'

            }
        }

        stage('application_down') {
            steps {
                sh 'docker-compose down'


            }
        }
    }
post {
        always {
            echo 'Always Hello!'
        }
        changed {
            echo 'Something changed Hello!'
        }
        success {
            echo 'Success Hello!'
        }
        failure {
            echo 'You failed no Hello for you!'
        }
    }
}
