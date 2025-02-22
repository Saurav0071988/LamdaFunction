import json

def lambda_handler(event, context):
    # TODO implement
   Country=json.loads(event['body'])['country']
    message="i love my {}".format(Country)
    return message
