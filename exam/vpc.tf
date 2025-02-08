
# Create a new resource for the custom vpc with the given name give it a cidr_bloc of 10.0.0.0/16
resource "aws_vpc" "custom_vpc" {
  count                = 1
  cidr_block           = var.vpc_cidr # Create a new vpc with this cidr block
  enable_dns_support   = true         # Enable DNS support
  enable_dns_hostnames = true         # Enable DNS hostnames

  tags = {
    "Name" = "${var.name}-custom-vpc",
  }
}

# Creaation of the public subnet for the VPC
resource "aws_subnet" "public_custom_subnet" {
  vpc_id                  = aws_vpc.custom_vpc[0].id # Attach the subnet to the VPC
  cidr_block              = var.public_subnet_cidr[0]
  map_public_ip_on_launch = true

  tags = {
    "Name" = "${var.name}-public-subnet",
  }
}

# Creation of the private subnet for the VPC
resource "aws_subnet" "private_custom_subnet" {
  vpc_id                  = aws_vpc.custom_vpc[0].id # Attach the subnet to the VPC
  cidr_block              = var.private_subnet_cidr[0]
  map_public_ip_on_launch = false

  tags = {
    "Name" = "${var.name}-private-subnet",
  }
}

# Creating a resource for internet gateway
resource "aws_internet_gateway" "main_igw" {
  vpc_id     = aws_vpc.custom_vpc[0].id
  depends_on = [aws_subnet.public_custom_subnet]
  tags = {
    "Name" = "${var.name}-internet-gateway",
  }
}

# Public and private route tables
# The public route table will have a route to direct traffic to the internet gateway(main_internet_gateway)
# The private route table will dnot have a route cause it does not need to direct any traffic to the internet
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.custom_vpc[0].id

  route {
    cidr_block = var.rt_cidr
    gateway_id = aws_internet_gateway.main_igw.id
  }

  tags = {
    "Name" = "${var.name}-public-rt",
  }
}
resource "aws_route_table" "private_rt" {
  vpc_id = aws_vpc.custom_vpc[0].id

  tags = {
    "Name" = "${var.name}-private-rt",
  }
}

# Associate the routing tables with the subnets (public and private)
resource "aws_route_table_association" "public_rt_association" {
  subnet_id      = aws_subnet.public_custom_subnet.id
  route_table_id = aws_route_table.public_rt.id
}
resource "aws_route_table_association" "private_rt_association" {
  subnet_id      = aws_subnet.private_custom_subnet.id
  route_table_id = aws_route_table.private_rt.id
}

# Create a aws security group
# Open port 22 for ssh ingress=inbound rules and egress=outbound rules
# Should open port 80
# NOT USED YET WILL USE IN THE SECOND STEP
resource "aws_security_group" "sg" {
  vpc_id      = aws_vpc.custom_vpc[0].id
  description = "Allow inbound traffic for SSH and HTTP"
  name        = "${var.name}-sg"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
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

# Creation of ec2 ubunto instance

# Output the vpc, public subnet, private subnet, internet gateway, public route table, private route table
