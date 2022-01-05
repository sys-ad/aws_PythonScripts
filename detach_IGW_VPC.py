# Detaches IGW to VPC
import boto3

ec2 = boto3.resource('ec2')
vpc = ec2.Vpc('vpc-xxx..')    # VPC identifier here
response = vpc.detach_internet_gateway(
    InternetGatewayI='igw-xxx...'    # igw-id goes here
)
