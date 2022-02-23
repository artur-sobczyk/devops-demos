# list all regions
# https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-regions.html

`aws ec2 describe-regions`
`aws ec2 describe-regions --output=table`
`aws ec2 describe-regions --debug`
`aws ec2 describe-regions --dry-run`

# filtering, constrains
#   - https://jmespath.org/
#   - https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html#cli-usage-filter-client-side-advanced
`aws ec2 describe-regions --query 'Regions[*]'`
`aws ec2 describe-regions --query 'Regions[0]'`
`aws ec2 describe-regions --query "Regions[?starts_with(RegionName, 'eu')]" --output=table`


# projection
`aws ec2 describe-regions --query 'Regions[].[RegionName, Endpoint]'`
`aws ec2 describe-regions --query 'Regions[0]'.RegionName --output text`
