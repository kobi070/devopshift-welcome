import jinja2
from python_terraform import Terraform
import sys
import os

class TerraformManager:
    def __init__(self, config):
        self.config = config
        self.tf = Terraform(working_dir='./generated')
        self.template_file = os.path.join(os.path.dirname(__file__), 'template', 'ec2_alb_template.tf.j2')

    def generate_terraform(self):
        print(f"Template file path: {self.template_file}")

        try:
            with open(self.template_file, 'r') as file:
                template = jinja2.Template(file.read())
        except FileNotFoundError:
            print(f"Template file not found: {self.template_file}")
            sys.exit(1)

        variables = self.config.to_dict()

        terraform_output = template.render(variables)
        print(f"Rendered Terraform Configuration:\n{terraform_output}")

        os.makedirs('generated', exist_ok=True)
        output_path = "generated/main.tf"
        print(f"Saving Terraform configuration to: {os.path.abspath(output_path)}")

        with open(output_path, "w") as output_file:
            output_file.write(terraform_output)

        print("Terraform configuration generated successfully.")
        return output_path

    def apply_terraform(self, terraform_file):
        if not os.path.exists(terraform_file):
            print("Error: main.tf does not exist. Exiting...")
            sys.exit(1)

        print("Initializing Terraform...")
        init_retcode, init_stdout, init_stderr = self.tf.init()
        print(init_stdout)
        if init_retcode != 0:
            print(f"Error during terraform init: {init_stderr}")
            sys.exit(1)

        print("Running terraform plan...")
        plan_retcode, plan_stdout, plan_stderr = self.tf.plan(destroy=False, out='plan.tfplan')
        print(plan_stdout)
        if plan_retcode != 0:
            print(f"Error during terraform plan: {plan_stderr}")
            sys.exit(1)

        print("Applying terraform configuration...")
        apply_retcode, apply_stdout, apply_stderr = self.tf.apply("plan.tfplan", capture_output=True, auto_approve=True)
        print(f"Apply Retcode: {apply_retcode}")
        print(apply_stdout)
        if apply_retcode != 0:
            print(f"Error during terraform apply: {apply_stderr}")
            sys.exit(1)

        print("\nCapturing Terraform output...")
        output = self.tf.output()
        print(f"Terraform outputs: {output}")

        instance_id = output.get('instance_id', {}).get('value', 'N/A')
        lb_dns_name = output.get('load_balancer_dns_name', {}).get('value', 'N/A')

        print(f"Instance ID: {instance_id}")
        print(f"Load Balancer DNS Name: {lb_dns_name}")

if __name__ == "__main__":
    terraform_manager = TerraformManager()
    terraform_file = terraform_manager.generate_terraform()
    terraform_manager.apply_terraform(terraform_file)
