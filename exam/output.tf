# Output the VPC ID
output "vpc_id" {
  description = "The ID of the custom VPC"
  value       = aws_vpc.custom_vpc[0].id
}

# Output the Public Subnet ID
output "public_subnet_id" {
  description = "The ID of the public subnet"
  value       = aws_subnet.public_custom_subnet.id
}

# Output the Private Subnet ID
output "private_subnet_id" {
  description = "The ID of the private subnet"
  value       = aws_subnet.private_custom_subnet.id
}

# Output the Internet Gateway ID
output "internet_gateway_id" {
  description = "The ID of the internet gateway"
  value       = aws_internet_gateway.main_igw.id
}

# Output the Public Route Table ID
output "public_route_table_id" {
  description = "The ID of the public route table"
  value       = aws_route_table.public_rt.id
}

# Output the Private Route Table ID
output "private_route_table_id" {
  description = "The ID of the private route table"
  value       = aws_route_table.private_rt.id
}

# Output the Security Group ID
output "security_group_id" {
  description = "The ID of the security group"
  value       = aws_security_group.sg.id
}

# Output the EC2 Instance ID (if you added the EC2 instance)
# output "ubuntu_instance_id" {
#   description = "The ID of the Ubuntu EC2 instance"
#   value       = aws_instance.ubuntu_instance.id
# }

# # Output the public IP of the Ubuntu EC2 instance (if applicable)
# output "ubuntu_instance_public_ip" {
#   description = "The public IP of the Ubuntu EC2 instance"
#   value       = aws_instance.ubuntu_instance.public_ip
# }

