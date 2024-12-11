import json
import boto3
from decimal import Decimal


def decimal_to_float(obj):
   """
   Convert DynamoDB Decimal objects to floats or ints.
   """
   if isinstance(obj, Decimal):
       # Convert to int if it's a whole number, otherwise to float
       if obj % 1 == 0:
           return int(obj)
       else:
           return float(obj)
   raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


def lambda_handler(event, context):
   dynamodb = boto3.resource('dynamodb')
   table = dynamodb.Table('Movies')


   # Fetch all movies
   response = table.scan()
   movies = response['Items']


   # Convert Decimal to standard Python types
   return {
       'statusCode': 200,
       'body': json.dumps(movies, default=decimal_to_float)  # Serialize using custom converter
   }
