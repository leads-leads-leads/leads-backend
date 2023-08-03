import json


def test(event, context):
    body = {
        "message": "andre and nick were here",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
