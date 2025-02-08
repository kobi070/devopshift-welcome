module "ec2_vpc" {
  source            = "./modules/ec2_vpc"
  vpc_cidr          = "10.0.0.0/16"
  instance_type     = "t2.micro"
  ami               = "ami-0e1bed4f06a3b463d"
  assigen_public_ip = true
  subnet_count      = 2
  subnet_cidr = {
    public  = ["10.0.1.0/24", "10.0.2.0/24"]
    private = ["10.0.3.0/24", "10.0.4.0/24"]
  }
}

output "ec2_vpc_output" {
  value       = module.ec2_vpc
  description = "outputs of the module"
}

module "app_alb" {
  source        = "./modules/alb"
  vpc_id        = module.ec2_vpc.vpc_id
  subnets       = module.ec2_vpc.public_subnet_ids
  instance_type = "t2.micro"
  ami           = "ami-0e1bed4f06a3b463d"
  depends_on = [ module.ec2_vpc ]
}

output "alb_output" {
  value = module.app_alb
}
