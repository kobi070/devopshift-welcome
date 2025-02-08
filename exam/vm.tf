# Creation of ec2 ubunto instance
resource "aws_instance" "ec2-ubuntu" {
  ami                         = var.ubuntu_ami # Ubuntu AMI
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.public_custom_subnet.id
  associate_public_ip_address = true
  security_groups             = [aws_security_group.sg.id]

  tags = {
    "Name" = "${var.name}-ec2-terraform"
  }
  depends_on = [aws_vpc.custom_vpc]
}
