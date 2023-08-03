import boto3
import json

s3 = boto3.client("s3")


def joinWaitlist(event, context):
    print(event)

    body = event["body"]
    print(body)

    email = body["email"]
    print(email)

    bucket = "triple-leads-mvp-emails"
    key = f"{email}.json"

    s3.put_object(Bucket=bucket, Key=key, Body=json.dumps(email))

    return {
        "statusCode": 200,
        "body": json.dumps(f"User {email} successfully added to the waitlist."),
    }
