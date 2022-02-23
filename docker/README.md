docker commands:

# build image
`docker build -t my-server .`

# run image
`docker run -d -p 8080:80 my-server`
`docker run -p 8080:80 my-server`
`docker run -it ubuntu bash`

# list all container
`docker container ls -a`

# list images
`docker image ls`

# stop
`docker container stop `

# clean up
`docker system prune -a`
`docker system prune --volumes`

# ECR

# list repos
`aws ecr describe-repositories --query repositories[].[repositoryName,createdAt] --output table`

# list images 
`aws ecr list-images --repository-name myhttpd --query imageIds[].[imageDigest,imageTag] --output table`

# create repo
`aws ecr create-repository --repository-name my-server`

# login
`aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 695414717878.dkr.ecr.eu-west-1.amazonaws.com`

# push image
# https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html
`docker tag my-server:latest 695414717878.dkr.ecr.eu-west-1.amazonaws.com/my-server:1.0`
`docker push 695414717878.dkr.ecr.eu-west-1.amazonaws.com/my-server:1.0`

# pull image
`docker pull 695414717878.dkr.ecr.eu-west-1.amazonaws.com/my-server-repo:my-server`

# delete repo
`aws ecr delete-repository --repository-name my-server`
