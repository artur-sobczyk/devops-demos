# create repo and set code
`aws codecommit create-repository --repository-name my-demo --repository-description "repository for demonstration"`

# setup git
```
    git clone https://git-codecommit.eu-west-1.amazonaws.com/v1/repos/my-demo
    cp -r ../codedeploy/StaticPage/* my-demo/
    cp buildspec.yml my-demo/

```




# delete repostory
`aws codecommit delete-repository --repository-name my-demo`



# links
- https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-basic-git.html