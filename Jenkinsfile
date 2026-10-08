pipeline {
    agent any
    environment {
        IMAGE_NAME = 'hello-docker'           // 镜像名
        REGISTRY   = 'localhost:5000'         // 私有仓库地址
        IMAGE_TAG  = "${BUILD_NUMBER}"        // 用构建号做版本
    }
    stages {
        stage('拉代码') {
            steps { checkout scm }            // 从 GitHub 拉代码
        }
        stage('打镜像') {
            steps { sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ." }
        }
        stage('推仓库') {
            steps {
                sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker push ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }
    }
}
