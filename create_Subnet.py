#Python3.7

# Creates a subnet in a specified VPC.
# Example usage: For greater redundency and network traffic control, you may have several subnets in different AZs.
import boto3
ec2 = boto3.resource('ec2')
vpc = ec2.Vpc('vpc-xxx..')       # The Vpc's Id identifier
subnet = vpc.create_subnet(
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'SubnetName'    # Subnet name goes here
                },
            ]
        },
    ],
    AvailabilityZone='us-east-1a',   # AZ ranges very by region
    #AvailabilityZoneId='use1-az1',    # AZ Id, varies. One way to check is through AWS CLI ----  $aws ec2 describe-availability-zones --region <your-region>
    CidrBlock='xxx.xxx.xxx.xxx/xx',    # Give the Subnet a CIDR block, should be within VPC CIDR
    DryRun=False,
    Ipv6Native=False
) 
