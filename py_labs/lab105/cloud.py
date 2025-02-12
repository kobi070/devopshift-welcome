from typing import Callable
import boto3
from botocore.exceptions import ClientError
from nice import print_title

def user_choice(menu: str, actions: dict[str, Callable]):
    while True:
        user_input = input(menu)
        if user_input == "q":
            break
        try:
            actions[user_input]()
        except KeyError:
            print("Unknown action, try again")


def list_buckets():
    s3_client = boto3.client("s3")
    response = s3_client.list_buckets()
    print("S3 Buckets:")
    for bucket in response["Buckets"]:
        print(f"- {bucket['Name']}")


def create_bucket():
    bucket_name = input("Enter bucket name: ")
    s3_client = boto3.client("s3")
    response = s3_client.create_bucket(Bucket=bucket_name)
    print(response)


def delete_bucket():
    bucket_name = input("Enter bucket name: ")
    s3_client = boto3.client("s3")
    try:
        response = s3_client.delete_bucket(Bucket=bucket_name)
        print(response)
    except ClientError:
        print("Bucket did not exist")


def list_instances():
    ec2_client = boto3.client("ec2")
    response = ec2_client.describe_instances()
    print(response)


def start_instance():
    instance_id = input("Enter instance ID: ")
    ec2_client = boto3.client("ec2")
    try:
        ec2_client.start_instances(InstanceIds=[instance_id])
    except ClientError:
        print("No such id")


def stop_instance():
    instance_id = input("Enter instance ID: ")
    ec2_client = boto3.client("ec2")
    try:
        ec2_client.stop_instances(InstanceIds=[instance_id])
    except ClientError:
        print("No such id")


def terminate_instance():
    instance_id = input("Enter instance ID: ")
    ec2_client = boto3.client("ec2")
    try:
        ec2_client.terminate_instances(InstanceIds=[instance_id])
    except ClientError:
        print("No such id")


def manage_s3():
    sub_menu = """What do you want to do to the buckets?
    1. List Buckets
    2. Create Bucket
    3. Delete Bucket
    q. BACK
    """
    user_choice(sub_menu, {"1": list_buckets, "2": create_bucket, "3": delete_bucket})


def manage_ec2():
    sub_menu = """What do you want to do to the Intances?
    1. List Intances
    2. Start Intance
    3. Stop Intance
    4. Terminate Intance
    q. BACK
    """

    user_choice(
        sub_menu,
        {
            "1": list_instances,
            "2": start_instance,
            "3": stop_instance,
            "4": terminate_instance,
        },
    )


main_menu = """What do you want to do?
1 - Manage S3 Buckets
2 - Manage EC2 Instances
3 OR q - Exit
"""

print_title("BOTO!")
user_choice(main_menu, {"1": manage_s3, "2": manage_ec2, "3": exit})