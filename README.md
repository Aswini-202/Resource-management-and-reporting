
# AWS Resource Management and Reporting

![Resource](https://github.com/Aswini-202/New_project/assets/132454046/582d20a1-2b08-4533-8452-6e76f3bb3be6)

## Overview

This project provides a solution for managing AWS resources, including EC2 instances and RDS databases, based on tags and generating reports via email using AWS Lambda, SNS (Simple Notification Service), and CloudWatch Events.

## Features

### 1. Schedule AWS Resources

- **Tag-Based Scheduling**: Resources are scheduled for start and stop operations based on specific tags.

- **EC2 Instance Management**: EC2 instances are started and stopped according to their schedule tags.

- **RDS Database Management**: RDS database instances are started and stopped as per their schedule tags.

### 2. Reporting of AWS Resources

- **Hashnode-Formatted Reports**: The project generates Hashnode-formatted reports detailing AWS resource information.

- **Email Notifications**: Reports are sent via email using AWS SNS.

## How It Works

### 1. Tagging Resources

Ensure that the AWS resources you want to schedule (EC2 instances and RDS databases) are appropriately tagged. For scheduling, a common tag like `Schedule` can be used.

### 2. Lambda Functions

Two Lambda functions have been created:

- **Start Resources Lambda**: This function is triggered by a CloudWatch Events rule to start resources based on their schedule tags.

- **Stop Resources Lambda**: This function is triggered to stop resources as per their schedule tags.

### 3. CloudWatch Events Rules

CloudWatch Events rules are configured to trigger the Lambda functions at scheduled intervals, based on the `Schedule` tags of the resources.

### 4. SNS for Notifications

- Amazon SNS topics are used to send notifications and reports.
  
- A Lambda function generates Hashnode-formatted reports and publishes them to an SNS topic.

- Subscribers to this topic receive reports via email.

## Setup Instructions

Follow these steps to set up and use the project:

1. **Tag Your Resources**: Ensure that your AWS resources are tagged appropriately with a `Schedule` tag.

2. **Lambda Configuration**: Create two Lambda functions - one for starting resources and one for stopping them. Customize the functions to match your AWS environment.

3. **CloudWatch Events Rules**: Configure CloudWatch Events rules to trigger the Lambda functions based on schedule tags.

4. **SNS Topics**: Create SNS topics for notifications and reports. Configure the Lambda function to publish reports to the desired SNS topic.

5. **Testing**: Test the setup by manually triggering CloudWatch Events rules and monitor Lambda executions.

6. **Email Subscriptions**: Subscribe to the SNS topic to receive Hashnode-formatted AWS resource reports via email.



```

