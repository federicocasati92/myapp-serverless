import json
import boto3

dynamodb = boto3.client('dynamodb')
TABLE_NAME = "ClickCounter"

def lambda_handler(event, context):
    try:
        response = dynamodb.update_item(
            TableName=TABLE_NAME,
            Key={
                'id': {'S': 'main'}
            },
            UpdateExpression="ADD visitCount :incr",
            ExpressionAttributeValues={
                ':incr': {'N': '1'}
            },
            ReturnValues="UPDATED_NEW"
        )
        
        visit_count = int(response['Attributes']['visitCount']['N'])
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'count': visit_count})
        }
    
    except Exception as e:
        print(f"Error updating DynamoDB: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': str(e)})
        }