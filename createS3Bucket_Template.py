import logging
import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    try:
        if region is not None:
            s3_cient = boto3.client('s3')
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
        else:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
     
    except ClientError as e:
        logging.error(e)
        return false
    return True
  
