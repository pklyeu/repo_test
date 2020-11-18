import os

def lambda_handler(event, context):

    print (event)
    response = {
        "statusCode": 200,
        "headers"   : {"Content-Type":"text/html; charset=utf-8"},
        "body"      : "<h2>its work</h2>"
    }

    return response
