import boto3

# Creating a single (1) message in SQS with custom attributes. 

queue = sqs.get_queue_by_name(QueueName='test') 

queue.send_message(MessageBody='boto3', MessageAttributes={
     'Author': {
          'StringValue': 'Daniel',
          'DataType': 'String'
     }
})
       
