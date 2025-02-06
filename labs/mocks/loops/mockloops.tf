# Testing diffrent capabilaties of loops if terraform
variable "aws_list" {
  default     = ["qa", "prod", "dev"]
  description = "A list for checking for loops in terraform"
}
variable "sec_aws_list" {
  default = [1,2,3,4]
  description = "another list of numbers"
}
variable "uppercase_aws_list" {
  default = ["A", "B", "C", "D"]
  description = "same list as aws_list but only upper case"
}
variable "verify_something" {
  type = set(string)
}

output "show_list" {
  value = {for x in var.aws_list : x => contains(var.verify_something, x)}
}