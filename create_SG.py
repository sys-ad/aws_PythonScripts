#Python3.x

# Creates security group

import boto3
client = boto3.client('ec2')
response = client.create_security_group(
    Description='Description',    # Description place holder
    GroupName='xxx',    # Security group name
    VpcId='xxx',    # Enter valid vpc-id
    TagSpecifications=[
        {
             'ResourceType': 'security-group',
             'Tags': [
                 {
                     'Key': 'Name',
                     'Value': 'xxx'    # Key:Value pair tag; 
                 },
              ]
        },
     ]
 )


