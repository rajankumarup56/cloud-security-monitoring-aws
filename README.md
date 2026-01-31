# Cloud Security Monitoring & Alerting on AWS

Real-time detection and alerting for suspicious AWS activity using native AWS services.
This project demonstrates security monitoring, alert automation, and DevOps best practices.

---

## Why this project?
In cloud environments, visibility and security monitoring are critical responsibilities of a DevOps engineer.
This project focuses on:
- Detecting suspicious or risky AWS actions
- Generating real-time alerts
- Applying least-privilege IAM principles
- Automating monitoring using Infrastructure as Code

---

## Architecture Overview
The monitoring pipeline works as follows:

1. AWS CloudTrail records account activity
2. Logs are sent to CloudWatch Logs
3. Metric filters detect suspicious events
4. CloudWatch Alarms are triggered
5. Alerts are delivered via SNS email notifications
6. Optional processing is handled using AWS Lambda

---

## Security Alerts Implemented
- Root account usage detection
- Unauthorized API calls
- AWS Console login failures
- IAM policy and role changes
- Security group modifications

---

## Tech Stack
- AWS CloudTrail
- AWS CloudWatch (Logs, Metric Filters, Alarms)
- Amazon SNS
- AWS Lambda
- IAM
- Terraform

---

## Infrastructure as Code
All AWS resources are provisioned using Terraform, ensuring:
- Repeatability
- Version control
- Minimal manual configuration

---

## Screenshots
Screenshots demonstrating active alarms and alert notifications are available in the `screenshots/` directory.

---

## Project Status
🚧 Actively improving
- Adding more alert scenarios
- Enhancing documentation
- Improving Terraform modularity

---

## Disclaimer
This project is created for learning and demonstration purposes.
It does not represent a production security system.
