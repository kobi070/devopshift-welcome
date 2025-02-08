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
variable "rt_cidr" {
  type        = string
  default     = "0.0.0.0/0"
  description = "value of the public route table cidr block which allows traffic"
}


# Module Varibles
# Module var for the user to chose which vpc cidr block to use
variable "vpc_cidr" {
  type        = string
  description = "value of the vpc cidr block"
}
# Moudle var for the user instance type
variable "instance_type" {
  type = string
  description = "value of the instance type"
}
# Moudle var for the user instance ec2 AMI choice
variable "ami" {
  type = string
  description = "value of the ubuntu ami"
}
# Module var for the user to chose whether a public id should be signed
variable "assigen_public_ip" {
  type = bool
  description = "value of the public ip"
}
# Module var for the user to chose the number of subnets he wishes to create
variable "subnet_count" {
  type = number
  description = "value of the number of subnets to create"
}
#  Module var for map of lists of strings (private, public) of subnets to cidr block to create for the subnet
variable "subnet_cidr" {
  type = map(list(string))
  default = {
    "public" = [],
    "private" = []
  }
  description = "a map of public and private subnets to cidr blocks"
}
