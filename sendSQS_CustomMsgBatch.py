import boto3

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='test')

response = queue.send_messages(Entries=[
    {           
        'Id': '1',                            # Creating, dictionaries with attributes and values.
        'MessageBody': 'world'
    },
    {
        'Id': '2',
        'MessageBody': 'boto3',
        'MessageAttributes': {               
            'Author': {
                'StringValue': 'Daniel',
                'DataType': 'String'
            }
        }
    }
])

print(response.get('Failed'))  # Print out any failured  -- Here, response retrives a list of successful/failed messages.
# print(response.get('Successful'))
