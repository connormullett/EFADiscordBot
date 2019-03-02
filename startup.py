
import sys
import boto3

from botocore.exceptions import ClientError


'''Demonstrating starting and stopping instances'''

# declaring system arguments
action =sys.argv[1]
instance_id = sys.argv[2]

ec2 = boto3.client('ec2')

# describe instances
response = ec2.describe_instances()
print(response)


def dry_run():
    try:
        ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise


if action == 'ON':
    # dry run to verify permissions
    dry_run()

    try:
        response = ec2.start_instances(InstanceIds=instance_id, DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

else:
    dry_run()

    # stop instances
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

