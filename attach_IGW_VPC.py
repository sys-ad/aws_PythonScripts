# Attach IGW to existing VPC

import boto3

ec2 = boto3.resource('ec2')
internet_gateway = ec2.InternetGateway('id')
response i


