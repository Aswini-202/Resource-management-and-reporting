AWSTemplateFormatVersion: '2010-09-09'
Resources:
  StartEC2Function:
    Type: AWS::Lambda::Function
    Properties:
      Handler: index.lambda_handler
      Role: !GetAtt StartEC2ExecutionRole.Arn
      FunctionName: StartEC2Function
      Code:
        ZipFile: |
          import boto3

          def lambda_handler(event, context):
              ec2_client = boto3.client('ec2', region_name='ap-south-1')

              # Start instances with 'test: yes' tag
              start_instances = ec2_client.describe_instances(Filters=[{'Name': 'tag:test', 'Values': ['yes']}])
              for reservation in start_instances['Reservations']:
                  for instance in reservation['Instances']:
                      instance_id = instance['InstanceId']
                      ec2_client.start_instances(InstanceIds=[instance_id])

      Runtime: python3.8

  StartEC2ExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: StartEC2Policy
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - ec2:DescribeInstances
                  - ec2:StartInstances
                Resource: '*'

  StartInstancesRule:
    Type: AWS::Events::Rule
    Properties:
      Description: "Scheduled rule to start EC2 instances"
      ScheduleExpression: "cron(40 19 * * ? *)"  # 01:40 AM IST (07:10 PM UTC)
      State: ENABLED
      Targets:
        - Arn: !GetAtt StartEC2Function.Arn
          Id: StartInstancesTarget

  StartInstancesPermission:
    Type: AWS::Lambda::Permission
    Properties:
      Action: lambda:InvokeFunction
      FunctionName: !Ref StartEC2Function
      Principal: events.amazonaws.com
      SourceArn: !GetAtt StartInstancesRule.Arn

  StopEC2Function:
    Type: AWS::Lambda::Function
    Properties:
      Handler: index.lambda_handler
      Role: !GetAtt StopEC2ExecutionRole.Arn
      FunctionName: StopEC2Function
      Code:
        ZipFile: |
          import boto3

          def lambda_handler(event, context):
              ec2_client = boto3.client('ec2', region_name='ap-south-1')

              # Stop instances with 'test: yes' tag
              stop_instances = ec2_client.describe_instances(Filters=[{'Name': 'tag:test', 'Values': ['yes']}])
              for reservation in stop_instances['Reservations']:
                  for instance in reservation['Instances']:
                      instance_id = instance['InstanceId']
                      ec2_client.stop_instances(InstanceIds=[instance_id])

      Runtime: python3.8

  StopEC2ExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: StopEC2Policy
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - ec2:DescribeInstances
                  - ec2:StopInstances
                Resource: '*'

  StopInstancesRule:
    Type: AWS::Events::Rule
    Properties:
      Description: "Scheduled rule to stop EC2 instances"
      ScheduleExpression: "cron(43 19 * * ? *)"  # 01:43 AM IST (07:13 PM UTC)
      State: ENABLED
      Targets:
        - Arn: !GetAtt StopEC2Function.Arn
          Id: StopInstancesTarget

  StopInstancesPermission:
    Type: AWS::Lambda::Permission
    Properties:
      Action: lambda:InvokeFunction
      FunctionName: !Ref StopEC2Function
      Principal: events.amazonaws.com
      SourceArn: !GetAtt StopInstancesRule.Arn
