terraform {
  required_providers {
    time = {
      source  = "hashicorp/time"
      version = "0.12.1"
    }
  }
}

provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-east-1"
}

# 2 ways to find an AMI id without having the ID
data "aws_ami" "terraformami" {
  owners = ["self"]
  filter {
    name = "name"
    values = ["terraform-workshop-image-do-not-delete"]
  }
  
}

data "aws_ami" "my-privateami" {
    owners = ["self"]  # Queries only AMIs owned by your account

}


# Create a var for the instance_id given to us
variable "instance_id" {
  description = "The ID of the EC2 instance"
  type        = string
  default     = "i-09df7e0ed385f871b"
}

# Fetch instance details based on instance ID
data "aws_instance" "yaniv_vm" {
  instance_id = var.instance_id
}

# Output the public IP
output "aws_yaniv_vm_public_ip" {
  value       = data.aws_instance.yaniv_vm.public_ip
  description = "Public IP of the specified instance"
}

# 2 ways Output
output "yanivsami" {
  value = data.aws_ami.my-privateami
}

output "terraformimage" {
  value = data.aws_ami.terraformami
}