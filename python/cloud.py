# imports
import boto3
import botocore
import botocore.exceptions

# S3 methods 
def list_buckets(s3_client: boto3.client) -> None: 
    try:
        response = s3_client.list_buckets()
        print("S3 Buckets:")
        for bucket in response['Buckets']:
            print(f" -{bucket['Name']}")
        print("\n")
    except botocore.exceptions.ClientError as err:
        print(f"Error: {err['error']['message']}")
def create_bucket(s3_client: boto3.client) -> None:
    bucket_name = input("Please enter a bucket name: ")
    try:
        if bucket_name not in s3_client.list_buckets():
            # Check if bucket already exists
            s3_client.create_bucket(bucket_name)
            print(f"Created bucket named: {bucket_name}\n")
        else:
            print(f"{bucket_name} already exists")
    except botocore.exceptions.ClientError as err:
        print(f"Error: {err['error']['message']}")
def delete_bucket(s3_client: boto3.client) -> None:
    bucket_name = input("Please enter a bucket name: ")
    try:
        s3_client.delete_bucket(
        Bucket = bucket_name)
        print(f"Deleted bucket: {bucket_name}\n")
    except botocore.exceptions.ClientError as err:
        print(f"Error: {err['error']['message']}")

# EC2 methods
def list_instances(ec2_client : boto3.client) -> None: 
    try:
        print(f"Your instances:")
        response = ec2_client.describe_instances()
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                print(f"Instance ID: {instance['InstanceId']} - State: {instance['State']['Name']}")
        print("\n")
    except botocore.exceptions.ClientError as err:
        print(f"Error: {err['error']['message']}")
def start_instance(ec2_client : boto3.client) -> None:
    instance_id = input("Enter instance ID: ")
    try:
        ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"Starting EC2 instance {instance_id}\n")
    except botocore.exceptions.ClientError as err:
        print(f"Error: {err['error']['message']}")
def delete_instance(ec2_client : boto3.client) -> None:
    instance_id = input("Enter instance ID: ")
    try:
        ec2_client.delete_instances(InstanceIds=[instance_id])
        print(f"Deleting EC2 instance {instance_id}\n")
    except botocore.exceptions.ClientError as err:
        print(f"Error: {err['error']['message']}")
def terminate_instance(ec2_client : boto3.client) -> None:
    instance_id = input("Enter instance ID: ")
    try:
        ec2_client.terminate_instances(InstanceIds=[instance_id])
        print(f"Terminating EC2 instance {instance_id}\n")
    except botocore.exceptions.ClientError as err:
        print(f"Error: {err['error']['message']}")

# Secondry Menus for EC2 and S3
def s3_menu():
    # Creating the S3 client
    s3_client = boto3.client("s3")
    s3_user_choice = input("1 List Buckets\n2.Create Bucket\n3.Delete Bucket\n[4/q].back\nYour choice: ")
    if s3_user_choice == "1":
        # "List Buckets"
        list_buckets(s3_client)
    elif s3_user_choice == "2":
        # "Create Bucket"
        create_bucket(s3_client)
    elif s3_user_choice == "3":
        # "Delete Bucket"
        delete_bucket(s3_client)
    elif s3_user_choice == "4" or s3_user_choice == "q":
        return menu()
def ec2_menu():
    ec2_client = boto3.client("ec2")
    ec2_user_choice = input("1 List Instances\n2.Create Instance\n3.Delete Instance\n4.Terminate Instance\n[5/q].back\nYour choice: ")
    if ec2_user_choice == "1":
        # "list instance"
        list_instances(ec2_client)
    elif ec2_user_choice == "2":
        # "start instance"
        start_instance(ec2_client)
    elif ec2_user_choice == "3":
        # "delete instance"
        delete_instance(ec2_client)
    elif ec2_user_choice == "4":
        # "Terminat a certain instance"
        terminate_instance(ec2_client)
    elif ec2_user_choice == "5" or ec2_user_choice == "q":
        return menu()

# Main menue
def menu():
    while True:
        user_input = input("Please Chose your operations: [1 - 3]\n1. Manage S3\n2. Manage EC2\n3. Exit\nYour choice: ")
        if user_input == "1":
            s3_menu()
        elif user_input == "2":
            ec2_menu()
        elif user_input == "3":
            exit()
            break
            
menu()
