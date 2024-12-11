import boto3

dynamodb = boto3.client('dynamodb')


response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'MovieID',
            'AttributeType': 'S'
        }
    ],
    TableName='Movie',
    KeySchema=[
        {
            'AttributeName': 'MovieID',
            'KeyType': 'HASH'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)
print(f'New resource created: {response['TableDescription']['TableName']}')
