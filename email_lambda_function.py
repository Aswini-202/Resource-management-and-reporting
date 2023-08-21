import json
import boto3
import datetime

def lambda_handler(event, context):
    client = boto3.client('ses', region_name='ap-south-1')
    ec2_client = boto3.client('ec2', region_name='ap-south-1')

    instance_id = 'i-0a5a9c026d12312ec'  # Replace with your specific instance ID

    email_body = f"Sample Summary Email:\n\n"
    email_body += f"Good Evening,\n\n"
    email_body += f"Here is a list of Resources running on your account as on {datetime.datetime.now()}:\n"

    # Extract EC2 instance tags for the specific instance ID
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            tags = instance.get('Tags', [])
            tag_string = ", ".join([f"{tag['Key']}: {tag['Value']}" for tag in tags])
            email_body += f"Instance ID: {instance_id}\nTags: {tag_string}\n"

    # Adding line breaks and additional content
    email_body += "\n\nThank You,\nKind Regards!\nTeam AWS"

    response = client.send_email(
        Destination={
            'ToAddresses': ['akshaykhanna7798@gmail.com']
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': email_body,
                }
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Sample Summary Email',
            },
        },
        Source='ick.june8@gmail.com'
    )

    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps("Email Sent Successfully. MessageId is: " + response['MessageId'])
    }
