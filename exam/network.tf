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