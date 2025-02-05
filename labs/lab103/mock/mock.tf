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
