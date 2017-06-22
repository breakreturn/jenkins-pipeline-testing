properties([parameters(
    [
        string(defaultValue: 'baz-mamifest', description: '', name: 'manifest'),
        string(defaultValue: 'baz-image', description: '', name: 'bitbake_image'),
        string(defaultValue: 'shamonkey', description: '', name: 'sha'),
        string(defaultValue: 'repomonkey', description: '', name: 'repo')
    ]), pipelineTriggers([])])



properties([
        [$class: 'ParametersDefinitionProperty', parameterDefinitions: [
            [
                $class: 'StringParameterDefinition',
                defaultValue: 'default-value',
                description: 'Parameter Text',
                name: 'manifest'
            ],
            [
                $class: 'StringParameterDefinition',
                defaultValue: 'default-value',
                description: 'Parameter Text',
                name: 'bitbake_image'
            ],
            [
                $class: 'StringParameterDefinition',
                defaultValue: 'default-value',
                description: 'git commit SHA',
                name: 'sha'
            ],
            [
                $class: 'StringParameterDefinition',
                defaultValue: 'default-value',
                description: 'git repo as <username/reponame>',
                name: 'repo'
            ]
        ]]
    ])


if (params.repo == "default-value") {
    currentBuild.displayName = "empty setup build"
    return
}

pipeline {
    agent any

    stages {
        stage('Download') {
            steps {
                checkout(
                    [$class: 'GitSCM',
                     branches: [[name: params.sha]],
                     userRemoteConfigs: [[url: 'https://github.com/' + params.repo + '.git']]
                    ])
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
