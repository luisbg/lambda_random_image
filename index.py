import json
import datetime
import boto3
import random

s3_client = boto3.client('s3')

def handler(event, context):
    print("Handle event %s" % event)

    objs = s3_client.list_objects_v2(Bucket="lbg-img")
    count = objs["KeyCount"]

    images = []
    for n in range(count):
        key = objs["Contents"][n]["Key"]
        if key.endswith(".jpg"):
            print(key)
            images.append(key)

    data = {
        'output': 'Random image',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'image': images[random.randint(0, count - 1)]
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
