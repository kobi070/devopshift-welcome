# Output the VPC ID
output "vpc_id" {
  description = "The ID of the custom VPC"
  value       = aws_vpc.custom_vpc[0].id
}

# Output the Public Subnet IDs
output "public_subnet_ids" {
  description = "The IDs of the public subnets"
  value       = [for subnet in aws_subnet.public_custom_subnet : subnet.id]
}

# Output the Private Subnet IDs
output "private_subnet_ids" {
  description = "The IDs of the private subnets"
  value       = [for subnet in aws_subnet.private_custom_subnet : subnet.id]
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

# Output the EC2 Instance IDs (if applicable)
output "ubuntu_instance_ids" {
  description = "The IDs of the Ubuntu EC2 instances"
  value       = [for ec2 in aws_instance.ec2-ubuntu : ec2.id]
}

# Output the public IPs of the Ubuntu EC2 instances (if applicable)
output "ubuntu_instance_public_ips" {
  description = "The public IPs of the Ubuntu EC2 instances"
  value       = [for ec2 in aws_instance.ec2-ubuntu : ec2.public_ip]
}
