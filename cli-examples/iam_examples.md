# links:
# - https://docs.aws.amazon.com/cli/latest/reference/iam/index.html#cli-aws-iam
# - https://docs.aws.amazon.com/cli/latest/reference/sts/

# check who I am
`aws sts get-caller-identity`

# looking for credentails
#   - https://awscli.amazonaws.com/v2/documentation/api/latest/topic/config-vars.html#credentials
`aws sts get-caller-identity --debug 2>&1 | grep credentials`

# info about role
`aws iam get-role --role-name s3_demo_role`
`aws iam list-attached-role-policies --role-name s3_demo_role`

# assume role
```
result=$(aws sts assume-role --role-arn arn:aws:iam::695414717878:role/s3_demo_role --role-session-name test | jq '.')

export AWS_ACCESS_KEY_ID=`echo $result | jq -r ".Credentials.AccessKeyId"`
export AWS_SECRET_ACCESS_KEY=`echo $result | jq -r ".Credentials.SecretAccessKey"`
export AWS_SESSION_TOKEN=`echo $result | jq -r ".Credentials.SessionToken"`

echo AWS_ACCESS_KEY_ID = $AWS_ACCESS_KEY_ID
echo AWS_SECRET_ACCESS_KEY = $AWS_SECRET_ACCESS_KEY 
echo AWS_SESSION_TOKEN = $AWS_SESSION_TOKEN

aws sts get-caller-identity

printenv
unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_ROLE_SESSION_NAME

```


