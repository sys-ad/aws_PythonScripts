#python3.7
import boto3


# Descibes specific VPC subnet. Check the API Documentation for further granulation of the Filters list

response = client.describe_subnets(
             Filters=[
                 {
                     'Name': 'vpc-id',
                     'Values': [
                         'vpc-xxx..',     # VPC id goes here
                     ],
                 },
              ],
           )
