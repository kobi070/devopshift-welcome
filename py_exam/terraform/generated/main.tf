provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = "10.0.${count.index}.0/24"
  availability_zone = element(["us-east-1a", "us-east-1b"], count.index) # Adjust for multiple AZs
  map_public_ip_on_launch = true
}

resource "aws_security_group" "lb_sg" {
  name        = "lb_security_group_${random_id.lb_sg_suffix.hex}"
  description = "Allow HTTP inbound traffic"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web_server" {
  ami               = "ami-0c518311db5640eff"
  instance_type     = "t3.small"
  availability_zone = element(["us-east-1a", "us-east-1b"], 0) # Choose a zone that has subnets
  subnet_id         = aws_subnet.public[0].id # Attach to the first subnet created
  tags = {
    Name = "WebServer"
  }
}

resource "aws_lb" "application_lb" {
  name               = "s"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.lb_sg.id]
  subnets            = aws_subnet.public[*].id
}

resource "aws_lb_listener" "http_listener" {
  load_balancer_arn = aws_lb.application_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.web_target_group.arn
  }
}

resource "aws_lb_target_group" "web_target_group" {
  name     = "web-target-group"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.main.id
}

resource "aws_lb_target_group_attachment" "web_instance_attachment" {
  target_group_arn = aws_lb_target_group.web_target_group.arn
  target_id        = aws_instance.web_server.id
}

resource "random_id" "lb_sg_suffix" {
  byte_length = 4
}