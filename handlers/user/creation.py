import json

def test(event, context):
    message = event.get("message", "No message found")

    body = {
        "message": "andre and nick were here",
        "input": event,
        "received_message": message,
    }

    print("please show up on cloudwatch")
    print(message)

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def createUser(event, context):
    response = {"statusCode": 200}

