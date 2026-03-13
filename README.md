# Cloud Security Monitoring on AWS

## Overview

This project demonstrates how to implement cloud security monitoring in an AWS environment using CloudTrail and Amazon CloudWatch. The goal is to detect suspicious activities and trigger automated alerts.

---

## Architecture

![Architecture](architecture-diagram.png)

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
- Create metric filters for detecting suspicious actions
- Configure CloudWatch alarms
- Send alerts through SNS notifications

---

## Implementation Steps

1. Enable CloudTrail for AWS account activity logging  
2. Send CloudTrail logs to CloudWatch Logs  
3. Create metric filters for suspicious events  
4. Configure CloudWatch alarms  
5. Set up SNS notifications for alerts  

---

## Screenshots

### CloudTrail Trail

![CloudTrail](screenshots/cloudtrail-trail.png)

### CloudWatch Log Group

![CloudWatch Logs](screenshots/cloudwatch-log-group.png)

### Metric Filter

![Metric Filter](screenshots/metric-filter.png)

### CloudWatch Alarm

![Alarm](screenshots/cloudwatch-alarm.png)

### SNS Email Notification

![SNS Alert](screenshots/sns-email-alert.png)

---

## Learning Outcomes

- Understanding AWS monitoring and logging
- Implementing security-focused cloud monitoring
- Automating alert notifications using SNS

---

## Author

Ranjan Kumar Upadhyay
