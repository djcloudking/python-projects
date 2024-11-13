### Streamlining CI/CD Cost Management with Python Scripts and AWS Lambda


**Scenario: Cost-Effective Management for AWS CI/CD Infrastructure**

Consider a DevOps team using a development lab for application testing, where AWS EC2 instances in the lab run continuously. Management raises concerns about the escalating costs, as these instances operate 24/7, even when the team isn’t working. 

**Solution Outline**

To address this, we can automate instance management by using a Python script combined with AWS Lambda. The script will target EC2 instances tagged as "Dev," stopping them outside of active work hours. Here’s how it’s done:

### Prerequisites
1. Knowledge of Python
2. CLI familiarity  
3. AWS configured with necessary IAM permissions.
4. Basic knowledge of AWS Lambda, EC2, and Boto3 documentation.

### Step 1: Define the Scope

Since costs are primarily associated with development environments, we’ll focus on EC2 instances tagged “Dev” in our solution. 

### Step 2: Write the Python Script

- Imports Boto3 to interact with AWS.

- Creates an EC2 client for a specified region.

- Fetches a list of all running instances.

- Filters for instances tagged “Dev” and stops them.

- Outputs the IDs of the stopped instances for verification.


### Step 3: Test the Script

Run the script manually to verify it’s stopping only the desired “Dev” instances. You’ll see confirmation of which instances were stopped, displayed both in the console and the EC2 dashboard.

### Step 4: Automate with AWS Lambda

1. In the Lambda console, create a new function with Python as the runtime.

2. Paste your Python script into the function’s code editor and save.

3. Use EventBridge to set a cron job to trigger the Lambda function according to your desired schedule.

### Step 5: Test the Lambda Function

Run the Lambda function to confirm it performs as expected. Check the EC2 dashboard to ensure that only "Dev" instances were stopped.

### Conclusion

With this automated solution, you’ve successfully managed the cost of your CI/CD environment, ensuring it serves the team’s needs without unnecessary expense or oversight. This approach minimizes manual intervention, optimizes performance, and keeps your DevOps processes streamlined.

