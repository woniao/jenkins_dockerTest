pipeline {
    agent any
    environment {
        // 注意！不再是 localhost，而是 1st 机的真实 IP
        REGISTRY   = '192.168.126.128:5000'
        IMAGE_NAME = 'hello-docker'
        IMAGE_TAG  = "${env.BUILD_NUMBER}"    // 每次构建号不同 → 触发滚动更新
    }
    stages {
        stage('拉代码') {
            steps { checkout scm }
        }
        stage('打镜像') {
            steps { sh "docker build -t ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} ." }
        }
        stage('推仓库') {
            steps { sh "docker push ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}" }
        }
        stage('部署到 K8s') {
            steps {
                // 把 deploy.yaml 里的 __TAG__ 占位符替换成真实构建号
                sh "sed -i 's/__TAG__/${IMAGE_TAG}/g' deploy.yaml"
                // kubectl 就在 1st（Master）本机，直接 apply
                sh 'kubectl apply -f deploy.yaml'
                // 阻塞等待滚动更新完成
                sh 'kubectl rollout status deployment/hello-web'
            }
        }
    }
    post {
        success { echo '全链路 CI/CD 成功！' }
        failure { echo '流水线失败，看日志定位' }
    }
}
