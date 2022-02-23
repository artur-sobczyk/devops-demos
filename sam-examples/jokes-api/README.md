# https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html

# build
`sam build --use-container`

# test localy
`sam local invoke JokeFunction`

# test in container
`sam local start-api`
`curl http://127.0.0.1:3000/joke`

# deploy
`sam deploy`

# delete
`sam delete`