# 🧩 AWS Serverless Web App – Architecture and Services (Customizable Template)

This template provides a structured overview of your AWS serverless project. Fill in the placeholders with your project-specific values.

---

## 📁 Amazon S3 – Static Website Hosting

- **Bucket Name:** `<YOUR_BUCKET_NAME>`
- **Public Access Enabled:** Yes / No
- **Index Document:** `index.html`
- **Endpoint URL:** `http://<S3_WEBSITE_ENDPOINT>`

**Security Notes:**
- Current bucket policy:
```json




<INSERT_YOUR_BUCKET_POLICY>
🌍 Amazon CloudFront
Distribution ID: <YOUR_CLOUDFRONT_DIST_ID>

Domain Name: https://<YOUR_CLOUDFRONT_DOMAIN>

S3 Origin Domain: <YOUR_S3_ORIGIN>

API Gateway Origin: <YOUR_API_ORIGIN>

Caching Settings: <STATIC / DYNAMIC>



🔐 AWS WAF – Web Application Firewall
Web ACL Name: <YOUR_WEB_ACL_NAME>

Associated Resources: CloudFront / API Gateway

Blocked IP Set: <YOUR_IP_SET_NAME>

Monitoring Metrics: <CLOUDWATCH_METRIC_NAMES>

Notification Topic ARN (SNS): <SNS_TOPIC_ARN>



👤 Amazon Cognito – User Authentication
User Pool ID: <YOUR_USER_POOL_ID>

App Client ID: <YOUR_APP_CLIENT_ID>

Hosted UI Domain: <YOUR_COGNITO_DOMAIN>

Login Callback URL: <YOUR_CALLBACK_URL>

Token Processing in Frontend: Extract id_token from window.location.hash



🚀 Amazon API Gateway – REST API
API Name: <YOUR_API_NAME>

Stage: <dev / prod>

Endpoint URL: https://<API_ID>.execute-api.<REGION>.amazonaws.com/<STAGE>/

Methods Enabled: POST, OPTIONS

CORS Settings:

Allowed Origins: * or specific domains

Allowed Headers: Content-Type, Authorization

Cognito Authorizer:

User Pool ID: <YOUR_USER_POOL_ID>

Token Source Header: Authorization: Bearer <id_token>



⚙️ AWS Lambda – Backend Function
Function Name: <YOUR_LAMBDA_FUNCTION_NAME>

Runtime: Python 3.x

Handler: lambda_function.lambda_handler

Connected API Endpoint: POST /update-visit

Code Snippet Template:

python
Copia
Modifica
token = event['headers']['Authorization'].split(" ")[1]
decoded = jwt.decode(token, options={"verify_signature": False})
user_id = decoded['sub']
# DynamoDB update logic
IAM Role ARN for Lambda: <LAMBDA_EXECUTION_ROLE>



🗃️ Amazon DynamoDB – NoSQL Storage
Table Name: ClickCounter

Primary Key: id (String)

Additional Attributes: visitCount (Number)

Provisioned Throughput / On-Demand: <YOUR_CHOICE>



📣 Amazon SNS – Notifications
Topic Name: <YOUR_SNS_TOPIC_NAME>

Recipients (Emails): <EMAIL_1>, <EMAIL_2>

CloudWatch Trigger: <METRIC_NAME or FILTER_PATTERN>

📊 Amazon CloudWatch – Logging and Metrics


Log Groups:

/aws/lambda/<YOUR_LAMBDA_FUNCTION_NAME>

API Gateway Execution Logs

Metric Filters: <EXAMPLES>

Alarms & Alerts: <EXAMPLES>



🔐 IAM – Roles & Policies
Lambda Execution Role: <ROLE_NAME>

Permissions Granted:

dynamodb:UpdateItem

logs:PutLogEvents

Least Privilege Review: ✅ / ❌



🔁 CORS Configuration
Allowed Origins: <http://your-frontend-domain>

Allowed Methods: GET, POST, OPTIONS

Allowed Headers: Authorization, Content-Type

