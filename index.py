import json
import datetime
import boto3
import random

s3_client = boto3.client('s3')

def handler(event, context):
    print("Handle event %s" % event)

    objs = s3_client.list_objects_v2(Bucket="lbg-img")
    print("amount of files: %s" % objs["KeyCount"])
    print("")

    for n in range(objs["KeyCount"]):
        print(objs["Contents"][n]["Key"])

    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
