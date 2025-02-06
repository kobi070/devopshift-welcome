module "ec2" {
    source = "./modules/ec2"
    region = "us-east-1"
    ami = "ami-0c02fb55956c7d316"
    instance_type = "t2.micro"
    tags = {Name: "kobi-vm"}
  
}
output "ec2_output" {
  value = module.ec2
}