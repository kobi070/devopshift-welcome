# This is the logic for the module/main.tf file
# The module main.tf will come to this file and insert the varibales values
# Example :
# region = "us-east-1"
# ami = "ami-0c02fb55956c7d316"
# instance_type = "t2.micro"
# tags = {Name: "kobi-vm"}

# Providers for terraform
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

# The generic/template varibales which we inject to using our modules/main.tf file
# For each of those varibales we let the user decide which region,ami,instance_type and tags
# for example we could have added a varibale for each of the rules we want to adress in our firewall using our security group

variable "region" {
  default = "us-east-1"
}
variable "ami" {
}

variable "instance_type" {
}
variable "tags" {
}

# Define the variable to accept a list of ports
variable "open_ports" {
  description = "List of open ports for the security group"
  type        = list(number)
}

# Define a security group resource using the ports
# Using for_each from terraform
resource "aws_security_group" "sg_ex" {
  name        = "example-security-group"
  description = "Security group for dynamic ports"

  dynamic "ingress" {
    for_each = var.open_ports

    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"             # Default protocol
      cidr_blocks = ["0.0.0.0/0"]    # Default CIDR block
    }
  }
}



# All the resource used for vars in our module
# Resource: time_sleep, null_resource, aws_security_group, aws_instance
# The modules/main.tf file will insert the user(or like in our example hard coded) into the vars we created
# afterwards in this file (ec2/main.tf) will create those resources and run them
# Could have created a varibale for each of the varibales inside the resources
# Example:
# we could create a varibale name ingress and egress and give the user the opprtunity to insert them
# Mock data for view:
#   ingress {
#     from_port   = 22
#     to_port     = 22
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

# variable "ingress" {
# }
# variable "egress" {
# }

resource "time_sleep" "wait_for_ip" {
  create_duration = "10s" # Wait for 10 seconds
}

resource "null_resource" "run_script" {
  provisioner "local-exec" {
    command = "echo 'Hello Jb Class'"
  }
}

resource "null_resource" "check_public_ip" {
  provisioner "local-exec" {
    command = <<EOT
      if [ -z "${aws_instance.vm.public_ip}" ]; then
        echo "ERROR: Public IP address was not assigned." >&2
        exit 1
      fi
    EOT
  }

  depends_on = [aws_instance.vm]
}

resource "aws_security_group" "sg" {
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "vm" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.sg_ex.id]

  tags = {
    Name = "kobi-vm"
  }
}

# Outputs of each varibale we get from our modules/main.tf file
# This is granted to uss cause of the output "ec2_output" in our modules/main.tf files
output "region" {
  value = "The region you chose ${var.region}"
}
output "ami" {
  value = "The ami you chose: ${var.ami}"
}
output "instance_type" {
  value = "The instance type you chose: ${var.instance_type}"
}

output "public_ip" {
  value = "The Public ip of the create machine: ${aws_instance.vm.public_ip}"
}
output "vm_public_ip" {
  value      = aws_instance.vm.public_ip
  depends_on = [null_resource.check_public_ip] # Wait for the time_sleep resource to complete
  # depends_on = [ time_sleep.wait_for_ip] # Wait for the time_sleep resource to complete
  description = "Public IP address of the VM"

}
