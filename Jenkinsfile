pipeline {
    agent any
    parameters {
        string(name: 'manifest', defaultValue: '', description: 'What repo manifest to use')
        string(name: 'bitbake_image', defaultValue: '', description: 'What image to build')
    }
    stages {
        stage('Download') {
            steps {
                echo "In Download"
                echo params.manifest
                echo params.bitbake_image
            }
        }
        stage('Build') {
            steps {
                script {
                    println "From a groovy script"
                }
            }
        }
    }
    post {
        always {
            echo "In post"
        }
    }
}
