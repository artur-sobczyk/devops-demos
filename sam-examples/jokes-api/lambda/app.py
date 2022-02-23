import random
import json

def lambda_handler(event, context):
   
    with open("./jokes.txt") as file:
        jokes = file.readlines()
   
    return {
        "statusCode": 200,
        "body": "\n" + jokes[random.randint(0,len(jokes)-1)] + "\n"
    }