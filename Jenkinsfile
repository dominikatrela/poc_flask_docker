pipeline {
    agent {
        label 'master'
    }
	environment {
        REPO_URL = "${POC_FLASK_DOCKER_REPO}"
	CREDENTIALS = "${GITHUB_CREDENTIALS_ID}"
	BRANCH_NAME = "${BRANCH_NAME}"
    }

    stages {

        stage('get_latest_version') {
            steps {
                deleteDir()
		    git branch: "${BRANCH_NAME}", credentialsId: CREDENTIALS, url: REPO_URL
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
                sh 'make run-gui-test'

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
