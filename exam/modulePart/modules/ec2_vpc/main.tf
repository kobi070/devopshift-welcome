# Module 
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
# TODO: add count cause user can provide multiple public subnets
resource "aws_subnet" "public_custom_subnet" {
  count                   = length(var.subnet_cidr["public"])
  vpc_id                  = aws_vpc.custom_vpc[0].id # Attach the subnet to the VPC
  cidr_block              = var.subnet_cidr["public"][count.index]
  map_public_ip_on_launch = true
  availability_zone = var.az-list[count.index]

  tags = {
    "Name" = "${var.name}-public-subnet-${count.index}",
  }
}

# Creation of the private subnet for the VPC
# TODO: add count cause the user can give you a few diffrent subnet ips
resource "aws_subnet" "private_custom_subnet" {
  count                   = length(var.subnet_cidr["private"])
  vpc_id                  = aws_vpc.custom_vpc[0].id # Attach the subnet to the VPC
  cidr_block              = var.subnet_cidr["private"][count.index]
  map_public_ip_on_launch = false
  availability_zone = var.az-list[count.index]

  tags = {
    "Name" = "${var.name}-private-subnet-${count.index}",
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
# TODO: add count cause the user can give you a few diffrent subnet ids
resource "aws_route_table_association" "public_rt_association" {
  count          = length(var.subnet_cidr["public"])
  subnet_id      = aws_subnet.public_custom_subnet[count.index].id
  route_table_id = aws_route_table.public_rt.id
}
resource "aws_route_table_association" "private_rt_association" {
  count          = length(var.subnet_cidr["private"])
  subnet_id      = aws_subnet.private_custom_subnet[count.index].id
  route_table_id = aws_route_table.private_rt.id
}




# Part 2 of the Terraform exam
# Createed a aws security group using aws_security_group resource
# Open port 22 for ssh ingress=inbound rules and egress=outbound rules
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

  tags = {
    "Name" = "${var.name}-instance-sg"
  }
}

# Creation of ec2 ubunto instance
resource "aws_instance" "ec2-ubuntu" {
  count                       = length(var.subnet_cidr["public"])
  ami                         = var.ami # Ubuntu AMI
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.public_custom_subnet[count.index].id
  associate_public_ip_address = var.assigen_public_ip
  security_groups             = [aws_security_group.sg.id]

  tags = {
    "Name" = "${var.name}-ec2-terraform-${count.index}"
  }
  depends_on = [aws_vpc.custom_vpc]
}
