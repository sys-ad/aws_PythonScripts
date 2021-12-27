import boto3

client = ec2.client.response()
response = client.create_route_table(
    DryRun=False,
    VpcId='vpc-xxx...',  # Enter Valid VPC ID
    TagSpecifications=[
        {
            'ResourceType': 'route-table',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Placeholder_Name'  # Give It a Name
                },
            ]
        }
    ]
)
