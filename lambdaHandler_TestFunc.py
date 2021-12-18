import json
def lambda_handler(event, context):
     message = 'Hello {} {}! Keep being AWSome Team Bamalam!'.format(event['first_name'], event['last_name'])
#print to CloudWatch logs
     print(message)
     return {
    'message' : message
}
  
