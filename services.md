``` 🧩 AWS Serverless Web App – Architecture and Services 

This provides a structured overview of your AWS serverless project. 

---

## 📁 Amazon S3 – Static Website Hosting

- **Bucket Name:** stsite3.com
- **Public Access Enabled:** Yes 
- **Index Document:** `index.html`
- **Endpoint URL:** `http://stsite3.com.s3-website-us-east-1.amazonaws.com`

**Security Notes:**
- Current bucket policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "*",
      "Resource": "arn:aws:s3:::stsite3.com/*"
    }
  ]
}
```


🌍 Amazon CloudFront
Distribution ID: E2MYBIFW24JUNI

Domain Name: dtn4bsrr7bbyf.cloudfront.net

S3 Origin Domain: stsite3.com.s3-website-us-east-1.amazonaws.com


Caching Settings: Custom caching ttl=0 for hands-on purpose

Response headers policy: Custom allowing https://us-east-1crtzroy18.auth.us-east-1.amazoncognito.com



🔐 AWS WAF – Web Application Firewall
Web ACL Name: block-my-ip

Associated Resources: CloudFront 

Blocked IP Set: block-my-ip

Monitoring Metrics: log groups: blockmyip  metric filter: blockmyip

Notification Topic ARN (SNS): arn:aws:sns:us-east-1:617842004789:Default_CloudWatch_Alarms_Topic



👤 Amazon Cognito – User Authentication
User Pool ID: us-east-1_crTZroY18

App Client ID: 7kob7less0v0j8qi36jnhd9o6g

Hosted UI Domain: https://us-east-1crtzroy18.auth.us-east-1.amazoncognito.com

Login Callback URL: https://dtn4bsrr7bbyf.cloudfront.net/

Token Processing in Frontend: Extract id_token from window.location.hash



🚀 Amazon API Gateway – REST API
API Name: My REST API  id=7ua2wf7t5b

Stage: prod

Endpoint URL: https://7ua2wf7t5b.execute-api.us-east-1.amazonaws.com/prod

Methods Enabled: POST, OPTIONS

CORS Settings:

Allowed Origins: * 

Allowed Headers: Content-Type, Authorization

Integration response: proxy lambda integration

Cognito Authorizer:

User Pool ID: User pool - 1wakzk - crTZroY18 (us-east-1)

Token Source Header: Authorization: Bearer <id_token>



⚙️ AWS Lambda – Backend Function
Function Name: clickcounterfunction

Runtime: Python 3.13

Handler: lambda_function.lambda_handler

Connected API Endpoint: POST /update-visit

token = event['headers']['Authorization'].split(" ")[1]
decoded = jwt.decode(token, options={"verify_signature": False})
user_id = decoded['sub']

# DynamoDB update logic
IAM Role ARN for Lambda: arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess
               



🗃️ Amazon DynamoDB – NoSQL Storage
Table Name: ClickCounter

Primary Key: id (String)

Additional Attributes: visitCount (Number)

Provisioned Throughput / On-Demand: on-Demand



📣 Amazon SNS – Notifications
Topic Name: Default_CloudWatch_Alarms_Topic

Recipients (Emails): federico.casati@outlook.com

CloudWatch Trigger: blockmyip



📊 Amazon CloudWatch – Logging and Metrics

Log Groups:

/aws/lambda/clickcounterfunction

API-Gateway-Execution-Logs_7ua2wf7t5b/prod

Metric filters: blockmyip (WAF)
Alarms & Alerts: blockmyip



🔐 IAM – Roles & Policies
Lambda Execution Role: AmazonDynamoDBFullAccess
                       AWSLambdaBasicExecutionRole-2fb97b34-3e84-440d-b4f3-8d370f8c2983 (logs)



🔁 CORS Configuration
Allowed Origins: *

Allowed Methods: GET, POST, OPTIONS

Allowed Headers: Authorization, Content-Type

