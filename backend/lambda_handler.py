import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    prompt = body.get("prompt", "")

    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
    response = bedrock.invoke_model(
        modelId="amazon.titan-text-lite-v1",
        body=json.dumps({
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 256,
                "temperature": 0.7,
                "topP": 0.9
            }
        }),
        contentType="application/json"
    )

    result = json.loads(response['body'].read())
    return {
        'statusCode': 200,
        'headers': {"Content-Type": "application/json"},
        'body': json.dumps({"answer": result['results'][0]['outputText']})
    }
