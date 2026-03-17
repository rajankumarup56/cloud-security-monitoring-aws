# Cloud Security Monitoring on AWS

🔹 Implemented real-time security monitoring using AWS CloudTrail, CloudWatch and SNS alerts.

---

## Architecture Diagram

![Architecture](architecture-diagram.png)

---

## Architecture Workflow

1. CloudTrail captures all API activity
2. Logs are sent to CloudWatch
3. Metric filters detect suspicious activity
4. CloudWatch Alarms trigger alerts
5. SNS sends email notifications

---

## AWS Services Used

* CloudTrail
* CloudWatch
* SNS
* S3

---

## Screenshots

## CloudTrail Logs

![CloudTrail](screenshots/cloudtrail-logs.png)

## CloudWatch Metrics

![CloudWatch](screenshots/cloudwatch-monitoring.png)

## Alarm Configuration

![Alarm](screenshots/alarm.png)

---

## Related Project

AWS Highly Available Web Architecture
https://github.com/rajankumarup56/aws-highly-available-web-architecture

---

## Author

Ranjan Kumar Upadhyay
