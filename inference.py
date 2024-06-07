import boto3
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use environment variables to configure the client
client = boto3.client(
    'bedrock-runtime',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_DEFAULT_REGION')
)

def get_model_response(prompt):
    input_data = {
        "modelId": "ai21.j2-mid-v1",
        "contentType": "application/json",
        "accept": "*/*",
        "body": json.dumps({
            "prompt": prompt,
            "maxTokens": 200,
            "temperature": 0.7,
            "topP": 1,
            "stopSequences": [],
            "countPenalty": {"scale": 0},
            "presencePenalty": {"scale": 0},
            "frequencyPenalty": {"scale": 0}
        })
    }
    
    response = client.invoke_model(contentType=input_data['contentType'], body=input_data['body'], modelId=input_data['modelId'])
    data = json.loads(response['body'].read().decode('utf-8'))
    return data.get('completions', [{}])[0].get('data', {}).get('text', 'No response')
