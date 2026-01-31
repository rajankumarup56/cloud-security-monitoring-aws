This architecture implements a security monitoring pipeline using AWS-native services.

CloudTrail captures all account activity and delivers logs to CloudWatch Logs.
Metric filters analyze logs to identify suspicious behavior such as unauthorized access or root account usage.
When thresholds are breached, CloudWatch Alarms trigger notifications through Amazon SNS.
Optional Lambda functions can process or enrich alerts before delivery.
