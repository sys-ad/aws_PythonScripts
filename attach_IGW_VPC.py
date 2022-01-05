# Attach IGW to existing VPC

import boto3

ec2 = boto3.resource('ec2')
internet_gateway = ec2.InternetGateway('igw-xxx')   # input valid internet gateway as a string
response = internet_gateway.attach_to_vpc(
    VpcId='string'  # The ID of the VPC
)


