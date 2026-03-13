# Cloud Security Monitoring on AWS

## Project Overview

This project demonstrates how to implement cloud security monitoring in an AWS environment using AWS CloudTrail and Amazon CloudWatch. The setup detects suspicious activities in the AWS account and automatically sends alerts using Amazon SNS.

---

## Architecture

![Architecture Diagram](architecture-diagram.png)

---

## AWS Services Used

- AWS CloudTrail
- Amazon CloudWatch
- Amazon SNS
- AWS IAM

---

## Key Features

- Monitor AWS account activity using CloudTrail
- Send logs to CloudWatch for monitoring
- Create metric filters to detect suspicious events
- Configure CloudWatch alarms
- Send automated alerts using SNS notifications

---

## Implementation Steps

1. Enable AWS CloudTrail to log account activities  
2. Send CloudTrail logs to CloudWatch Logs  
3. Create metric filters for detecting suspicious activities  
4. Configure CloudWatch alarms based on the metric filters  
5. Set up SNS notifications to receive email alerts  

---

## Architecture Flow

User Activity  
↓  
AWS CloudTrail  
↓  
CloudWatch Logs  
↓  
Metric Filter  
↓  
CloudWatch Alarm  
↓  
SNS Notification  
↓  
Email Alert  

---

## Screenshots

### CloudTrail Dashboard

![CloudTrail](screenshots/cloudtrail-dashboard.png)

### CloudWatch Metric Filter

![Metric Filter](screenshots/metric-filter.png)

### CloudWatch Alarm Configuration

![CloudWatch Alarm](screenshots/cloudwatch-alarm.png)

### SNS Notification Setup

![SNS Notification](screenshots/sns-notification.png)

---

## Learning Outcomes

- Understanding AWS logging and monitoring
- Implementing security monitoring in AWS
- Creating automated alerting systems
- Improving cloud security visibility

---

## Author

Ranjan Kumar Upadhyay
