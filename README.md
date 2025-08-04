# Serverless ClickCounter WebApp on AWS

This project demonstrates a secure and scalable **serverless web application architecture** on AWS, combining a static frontend with an authenticated backend and cloud-native alerting features.

## 🔧 Architecture Overview

![Architecture Diagram](./aws_architecture_diagram.png)

**Key Components:**

- **S3 + CloudFront:** static hosting of the frontend with CDN acceleration
- **WAF (Web Application Firewall):** protects CloudFront from malicious IPs
- **Cognito User Pool:** user authentication and token generation
- **API Gateway:** exposes the backend as a REST API with Cognito-based authorization
- **Lambda:** handles logic to update click counts and trigger alerts
- **DynamoDB:** NoSQL table for storing click counts
- **CloudWatch + SNS:** monitors suspicious activity and sends notifications

## Accesso alla Web App

Puoi accedere alla web app pubblica tramite il seguente link CloudFront:  
[https://dtn4bsrr7bbyf.cloudfront.net/](https://dtn4bsrr7bbyf.cloudfront.net/)

### Login con Amazon Cognito

L'app utilizza Amazon Cognito per l'autenticazione degli utenti.  

Per effettuare il login, puoi usare uno dei seguenti account di test:

- **Username:** testuser1@example.com  
  **Password:** PasswordTest123!!


## 🔐 Security Features

- API access protected via **Amazon Cognito JWT tokens**
- **AWS WAF** blocks IPs based on custom rules
- **CloudWatch Alarms + SNS** send alerts on WAF rule matches

## 📁 File Structure

/frontend --> Static website files (HTML, JS, Cognito integration)
/backend --> Lambda function code
/docs/waf-cloudwatch-sns.md --> Detailed security/alerting logic
/screenshots --> AWS console screenshots (to be added)

markdown
Copia
Modifica

## 🚀 How to Deploy

This is a manual deployment project (no IaC yet). Main steps:

1. Upload frontend files to S3, enable static hosting
2. Set up CloudFront with S3 origin and WAF association
3. Configure Cognito User Pool and App Client
4. Create REST API in API Gateway with Cognito authorizer
5. Create Lambda function, grant necessary permissions
6. Set up DynamoDB table for click storage
7. Define WAF rules and CloudWatch alarms

## 📷 AWS Console Screenshots

Puoi trovare tutti gli screenshot organizzati per servizio nella cartella:  
[/screenshots/](./screenshots/)


## 📚 Technologies Used

- Amazon S3, CloudFront, WAF
- AWS Lambda, API Gateway, DynamoDB
- Amazon Cognito
- Amazon CloudWatch + SNS

## 🧠 Learning Outcome

- Designing real-world serverless architecture
- Secure API development with JWT authorization
- Alerting and logging integration via native AWS services
- Full end-to-end authentication and data handling in the cloud
