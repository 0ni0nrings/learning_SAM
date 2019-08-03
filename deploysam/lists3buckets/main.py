import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        #print(bucket["Name"])
        return {
        "statuscode": 200,
        "body": json.dumps(
            {"message": bucket["Name"]}
        )
    }
