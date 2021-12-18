import boto3 # Import python SDK Boto3 for AWS 

sqs = boto3.resource('sqs') # retrive sqs resource
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'}) # Creating queue; giving it a name and setting attribute(s).
                                                                             # This returns an SQS.Queue instance
print(queue.url)
print(queue.attributes.get('DelaySeconds'))
