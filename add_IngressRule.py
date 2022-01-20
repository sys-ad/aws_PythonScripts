#Python3.x

import boto3

# Adds the specified inbound rule(s) to a security group

client = boto3.client('ec2')

response = client.authorize_security_group_ingress()


--- update this
