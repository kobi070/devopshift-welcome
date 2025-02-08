variable "name" {
  default = "kobi"
  type    = string
}

resource "aws_security_group" "alb_sg" {
  name        = "${var.name}-alb-sg"
  description = "Allow inbound HTTP from ALB"
  vpc_id      = var.vpc_id
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

resource "aws_lb_target_group" "alb_tg" {
  name        = "${var.name}-alb-tg"
  target_type = "instance"
  port        = 80
  protocol    = "TCP"
  vpc_id      = var.vpc_id
}

resource "aws_lb" "app_lb" {
  name               = "${var.name}-alb"
  internal           = false
  load_balancer_type = "application"
  subnets            = var.subnets
  security_groups    = [aws_security_group.alb_sg.id]

}

resource "aws_launch_template" "app_launch_template" {
  name          = "${var.name}-app-launch-configuration"
  image_id      = var.ami
  instance_type = var.instance_type
  #   security_group_names = [aws_security_group.alb_sg.name]
  key_name               = "kobi-key-1"
  vpc_security_group_ids = [aws_security_group.alb_sg.id]

  tag_specifications {
    resource_type = "instance"
    tags = {
      Name = "${var.name}-app-instance"
    }
  }
}

resource "aws_autoscaling_group" "asg" {
  desired_capacity          = 1
  max_size                  = 3
  min_size                  = 1
  vpc_zone_identifier       = var.subnets
  target_group_arns         = [aws_lb_target_group.alb_tg.arn]
  health_check_type         = "ELB"
  health_check_grace_period = 300
  launch_template {
    id      = aws_launch_template.app_launch_template.id
    version = "$Latest"
  }
}
