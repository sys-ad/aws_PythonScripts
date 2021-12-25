import boto3

client = boto3.client('ec2')

response = client.create_vpc(
    CidrBlock='xxx.xxx.xxx.xxx/xx',
    InstanceTenancy='default',
    TagSpecifications=[
        {
            'ResourceType': 'vpc',     # 'ResourceType': 'xxx' | 'xxx' | ... |
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'NameofVPCxxx'    # Value is name of VPC
                }
            ]
        },
    ]
)


                  
