# Global Providers and Varibales
provider "aws" {
 region = var.region
}

variable "region" {
 default = "us-east-1"
}

data "aws_ami" "terraformami" {
  owners = ["self"]
  filter {
    name = "name"
    values = ["terraform-workshop-image-do-not-delete"]
  }
  
}

variable "ami" {
 default = "ami-0ecc0e0d5986a576d"
}

variable "vm_name" {
 default = "vm-kobi"
}

variable "admin_username" {
 default = "admin-user"
}

variable "admin_password" {
 default = "Password123!"
}

variable "vm_size" {
 default = "t2.micro"
}