# deploy to S3
`SRC_BUCKET=artsobcz-deployments-src`

# create bucket for deployment
`aws s3 mb s3://$SRC_BUCKET`

# create artifcat
`7z a -r StaticPage.zip ./StaticPage/*`

# deploy artifact to s3
`aws deploy push --application-name CodeDeploy-Demo --source StaticPage --s3-location s3://$SRC_BUCKET/StaticPage.zip`

```
aws deploy create-deployment \
    --application-name StaticPage \
    --deployment-group-name StaticPage-Deployment \
    --deployment-config-name CodeDeployDefault.AllAtOnce \
    --description "new deployment" \
    --s3-location bucket=$SRC_BUCKET,key=StaticPage.zip,bundleType=zip
```


# prepare instances
# https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-linux.html

```
#!/bin/bash
sudo yum update
sudo yum install ruby
sudo yum install wget

cd /home/ec2-user
wget https://aws-codedeploy-eu-west-1.s3.eu-west-1.amazonaws.com/latest/install
chmod +x ./install

sudo ./install auto
sudo service codedeploy-agent start

```