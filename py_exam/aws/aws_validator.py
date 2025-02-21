import boto3
import json

class AWSValidator:
    def __init__(self, instance_id, lb_dns_name):
        self.instance_id = instance_id
        self.lb_dns_name = lb_dns_name
        self.ec2 = boto3.client('ec2')
        self.elb = boto3.client('elbv2')

    def validate(self):
        # Fetch EC2 instance details
        instance = self.ec2.describe_instances(InstanceIds=[self.instance_id])['Reservations'][0]['Instances'][0]
        instance_state = instance['State']['Name']
        public_ip = instance.get('PublicIpAddress', 'N/A')

        # Fetch Load Balancer details
        load_balancer = self.elb.describe_load_balancers(Names=[self.lb_dns_name])['LoadBalancers'][0]
        load_balancer_dns = load_balancer['DNSName']

        # Store validation data in JSON
        validation_data = {
            "instance_id": self.instance_id,
            "instance_state": instance_state,
            "public_ip": public_ip,
            "load_balancer_dns": load_balancer_dns
        }

        with open("aws_validation.json", "w") as json_file:
            json.dump(validation_data, json_file, indent=4)

        print(f"Validation data saved to aws_validation.json.")

if __name__ == "__main__":
    validator = AWSValidator(instance_id="some-id", lb_dns_name="some-dns")
    validator.validate()
