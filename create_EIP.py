import boto3
client = boto3.client('ec2')
response = client.allocate_address(
    Domain='vpc',
    TagSpecifications=[
        {
            'ResourceType': 'elastic-ip',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'EIP_NameGoesHere'
                },
            ]
        },
    ]
)
