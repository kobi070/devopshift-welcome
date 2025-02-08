# Condition varibles
variable "create_vpc" {
  type    = bool
  default = true
}

variable "create_ec2" {
  type    = bool
  default = true
}

variable "create_public_subnet" {
  type    = bool
  default = true
}

variable "create_private_subnet" {
  type    = bool
  default = true
}

variable "create_internet_gateway" {
  type    = bool
  default = true
}

# Varibale for availability zone
variable "az" {
  type        = string
  default     = "us-east-1a"
  description = "value of the availability zone"
}

# Name varibale
variable "name" {
  default = "kobi"
}

#  Creation of a few varibales for cidr blocks
variable "public_subnet_cidr" {
  type        = list(string)
  default     = ["10.0.1.0/24"]
  description = "value of the public subnet cidr block"
}
variable "private_subnet_cidr" {
  type        = list(string)
  default     = ["10.0.2.0/24"]
  description = "value of the private subnet cidr block"
}
variable "vpc_cidr" {
  type        = string
  default     = "10.0.0.0/16"
  description = "value of the vpc cidr block"
}
variable "rt_cidr" {
  type        = string
  default     = "0.0.0.0/0"
  description = "value of the public route table cidr block which allows traffic"
}