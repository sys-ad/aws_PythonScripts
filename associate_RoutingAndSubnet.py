#Python3.7

# Associate Routing-Table to Subnet within AWS VPC.

client = boto3.client('ec2')
response = client.associate_route_table(
    DryRun=False,
    RouteTableId='rtb-example'   # Route-table Id and subnet-Id found in IAM Console
    SubnetId='subnet-example'    
)

