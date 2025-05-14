# Import the boto3 library, which is the AWS SDK for Python.
import boto3

# Set the AWS region that this script will operate in.
region = 'us-east-2'

# Define the main handler function for the Lambda service.
# The 'event' parameter is used to pass in event data to the handler.
# The 'context' parameter provides information about the invocation, function, and execution environment.
def lambda_handler(event, context):
    # Create an EC2 client. 
    ec2 = boto3.client('ec2', region_name=region)

    # Initialize an empty list to store instance IDs.
    instanceids = []

    # Call the describe_instances method to retrieve information about all EC2 instances.
    response = ec2.describe_instances()

    # Iterate over the response from the describe_instances call.
    for reservations in response['Reservations']:
        # Each reservation in the response contains information about EC2 instances.
        for instance in reservations["Instances"]:
            # Check if the instance has any tags.
            if "Tags" in instance:
                # Iterate over the tags of the instance.
                for tag in instance["Tags"]:
                    # If a tag with the value 'Dev' is found, it will add the InstanceId to the variable 'instanceids'.                    
                    if tag["Value"] == 'Dev':
                        # Print the instanceids list. 
                        print(instanceids.append(instance['InstanceId']))
    #shut down described instances.
    response = ec2.stop_instances(InstanceIds=instanceids)