📦 System Architecture

AWS Architecture
Main Components:

    S3: Hosting the static HTML website.

    CloudFront + WAF: Global CDN + firewall to block suspicious IPs.

    Amazon Cognito: User authentication with Hosted UI.

    API Gateway: REST entry point protected by Cognito Authorizer.

    AWS Lambda: Serverless function to update the visit counter.

    DynamoDB: NoSQL database to store the counter.

    SNS + CloudWatch: Logging and notifications for security and monitoring.

🚀 Features

    Secure login via Amazon Cognito.

    APIs protected by JWT token (id_token).

    Update of the visit counter for each user.

    Protection from malicious IPs with WAF + SNS notifications.

    Static hosting of the HTML site via S3 + CloudFront.

🛡️ Security

    Access to the site through CloudFront, with S3 not directly accessible.

    JWT token validation via Cognito Authorizer.

    IAM policies following the principle of least privilege.

    Email notifications in case of IP blocking via AWS SNS.

📊 Monitoring

    CloudWatch Logs for Lambda, API Gateway, and WAF.

    Custom metrics for number of visits and blocked IPs.

    SNS configured to send email alerts.

🔧 Next Steps

    Restrict CORS to specific origins.

    Optimize CloudFront cache for static resources.

    Add federated login (Google, Facebook) via Cognito.

    Admin dashboard to view counters and logs.

📁 File Structure

    index.html – Static page with login button.

    lambda_function.py – Lambda function for counter.

    aws_architecture_diagram.png – Architecture diagram.

    README.md – This file.

    services.md – Summary of services in my project.

✅ Requirements

    AWS account with permissions on S3, Cognito, Lambda, API Gateway, DynamoDB, CloudFront.

    AWS CLI configured.

    Python 3.x for Lambda.

📌 Notes

Make sure IAM, CORS, and WAF configurations are thoroughly tested before deploying to production environment.
