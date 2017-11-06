import json
import datetime
import boto3
import random

s3_client = boto3.client('s3')

def handler(event, context):
    print("Handle event %s" % event)

    objs = s3_client.list_objects_v2(Bucket="lbg-img")
    count = objs["KeyCount"]
    print("amount of files: %s" % count)
    print("")

    for n in range(count):
        print(objs["Contents"][n]["Key"])

    data = {
        'output': 'Random image',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'image': objs["Contents"][random.randint(0, count)]["Key"]
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
