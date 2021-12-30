#python3.7

import boto3

client = boto3.client('ec2')
response = client.describe_subnets(
    SubnetIds=[input('Enter valid subnet-id: ')],    # Enter valid subnet-id here. SubnetId is a list; may input more subnet-id(s).
)

print(response)

