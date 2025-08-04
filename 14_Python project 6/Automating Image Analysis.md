# Automating Image Analysis in a Photo-Sharing Application  *Using AWS Lambda, S3, Rekognition, and DynamoDB with CDK and Python*  

---

## Overview

This tutorial shows how to use AWS CDK with Python to automate an image analysis workflow. The project demonstrates a serverless solution that analyzes images uploaded to an S3 bucket, extracts metadata using AWS Rekognition, and stores the results in DynamoDB. AWS Lambda orchestrates the processing, and CDK automates the infrastructure deployment.

---

## Scenario

Imagine you have a photo-sharing app where users upload images. You want each image to be automatically analyzed for key details like objects and scenes, and then save that information so users can view metadata about their photos.

---

## Architecture

- **S3 Bucket**: Stores uploaded images  
- **AWS Lambda**: Triggered on image upload, runs the analysis and saves results  
- **AWS Rekognition**: Performs image analysis  
- **DynamoDB**: Stores metadata results  
- **AWS CDK (Python)**: Defines and deploys the infrastructure  

---

## Prerequisites

- AWS account with admin privileges  
- Basic knowledge of AWS CDK, Python, and JavaScript  

---

## Setup Steps

### Step 1: Install AWS CDK

1. Open AWS CloudShell  
2. Run:  
   ```bash
   sudo npm install -g aws-cdk-lib
````

3. Create project directory and initialize CDK app:

   ```bash
   mkdir cdk-app
   cd cdk-app
   cdk init app --language python
   ```
4. Verify setup:

   ```bash
   cdk ls
   ```

### Step 2: Configure CDK Stack

1. Navigate to `lib` folder:

   ```bash
   cd lib
   ```
2. Replace existing stack file:

   ```bash
   rm cdk-app-stack.js
   touch cdk-app-stack.js
   nano cdk-app-stack.js
   ```
3. Copy content from this [CDK stack file](https://github.com/djcloudking/python-challenges/blob/main/95_Python%20project%206/lib/cdk-app-stack.js) and paste into `cdk-app-stack.js`.
4. Save and verify content:

   ```bash
   cat cdk-app-stack.js
   ```

### Step 3: Setup Lambda Function

1. Return to project root and create lambda directory:

   ```bash
   cd ..
   mkdir lambda && cd lambda
   ```
2. Create Python handler:

   ```bash
   touch index.py
   nano index.py
   ```
3. Copy Python Lambda code from [this repo](https://github.com/djcloudking/python-challenges/blob/main/95_Python%20project%206/lambda/index.py) into `index.py`.
4. Verify with:

   ```bash
   cat index.py
   ```

### Step 4: Bootstrap CDK

1. Bootstrap the environment:

   ```bash
   cdk bootstrap
   ```
2. If prompted for environment name, provide your AWS environment.

### Step 5: Synthesize CloudFormation Template

1. Generate CloudFormation template:

   ```bash
   cdk synth
   ```
2. Confirm template is created by checking AWS CloudFormation console.

### Step 6: Deploy CDK Stack

1. Deploy your stack:

   ```bash
   cdk deploy
   ```
2. Confirm deployment by typing `Y` if prompted.

---  

## Verification

1. Open the AWS S3 console.
2. Upload an image to the S3 bucket created by CDK.
3. Go to DynamoDB console and check the table for analysis results of the uploaded image.

**Expected outcome:** Lambda triggers on upload, Rekognition analyzes the image, and results are saved in DynamoDB.

--- 

## Summary

You’ve built a serverless pipeline that automates image analysis and metadata storage using AWS services and CDK in Python. This setup can be expanded for more complex use cases or scaled for production environments.

--- 

## Resources

* [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
* [AWS Rekognition](https://aws.amazon.com/rekognition/)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [AWS DynamoDB](https://aws.amazon.com/dynamodb/)

 ---

*Feel free to open issues or submit pull requests for improvements!*
 

