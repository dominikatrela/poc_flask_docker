pipeline {
    agent any

    stages {

        stage('get_latest_version') {
            steps {
                deleteDir()
                git branch: 'master',
                credentialsId: 'dominikatrela',
                url: 'https://github.com/dominikatrela/poc_flask_docker/'
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
                sh 'sleep 1'
                sh './check_for_200.sh'

            }
        }

        stage('test_page') {
            steps {
                sh 'sleep 1'
                sh './test_hits.sh'

            }
        }

        stage('application_down') {
            steps {
                sh 'docker-compose down'


            }
        }
    }
}