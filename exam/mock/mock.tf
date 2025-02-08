provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-east-1"
}

data "aws_vpc" "vpc_test" {
}

data "aws_subnet" "subnet_test" {
}

data "aws_internet_gateway" "internet_gateway_test" {
}
data "aws_route_table" "route_tables_test" {

}

output "vpc_output" {
  value = data.aws_vpc.vpc_test
}
output "subnet_output" {
  value = data.aws_subnet.subnet_test
}
output "internet_gateway_output" {
  value = data.aws_internet_gateway.internet_gateway_test

}
output "route_table_output" {
  value = data.aws_route_table.route_tables_test
}