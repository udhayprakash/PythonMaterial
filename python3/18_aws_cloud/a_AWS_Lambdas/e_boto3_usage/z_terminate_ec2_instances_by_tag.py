import boto3

ec2 = boto3.client("ec2", region_name="us-east-1")


def is_dev(instance):
    tag = {"Key": "Environment", "Value": "Dev"}
    is_dev = False
    if tag in instance["Tags"]:
        is_dev = True
    return is_dev


def is_running(instance):
    is_running = False
    if instance["State"]["Name"] == "running":
        is_running = True
    return is_running


instance_attr = ec2.describe_instances()

reservations = instance_attr["Reservations"]


def lambda_handler(event, context):
    for reservation in reservations:
        for instance in reservation["Instances"]:
            if is_dev(instance) and is_running(instance):
                instance_id = instance["InstanceId"]
                ec2.stop_instances(InstanceIds=[instance_id])


# IAM Policy - Lambda_Policy_Stop_Instance
