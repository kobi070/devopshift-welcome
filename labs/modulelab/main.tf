# Creation of a module based on the file inside the folder ec2
# We insert the certain values we want to the main.df in the ec2/main.df vars
# output the module varibales we inserted to the user
# See ec2/main.tf for extra documentation

module "ec2" {
    source = "./modules/ec2"
    
    # The vars to insert to the ec2/main.tf
    region = "us-east-1"
    ami = "ami-0c02fb55956c7d316"
    instance_type = "t2.micro"
    tags = {Name: "kobi-vm"}
  
}
output "ec2_output" {
  value = module.ec2
}