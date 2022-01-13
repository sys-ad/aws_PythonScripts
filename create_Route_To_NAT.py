#Python3.x

import boto3

ec2 = boto3.resource('ec2')
route_table = ec2.RouteTable('id')    # rt-id MUST be set
# Creates route in existing route table

route = route_table.create_route(
    DestinationCidrBlock='0.0.0.0/0',    # Check this,
    NatGatewayId='xxx'
)
