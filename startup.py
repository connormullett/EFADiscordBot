
import boto3

#start instance
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)

