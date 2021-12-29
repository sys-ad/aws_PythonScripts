#Python3.7

# Creates a subnet in a specified VPC.
# Example usage: For greater redundency and network traffic control, you may have several subnets in different AZs.
import boto3
ec2 = boto3.resource('ec2')
vpc = ec2.Vpc('id')
