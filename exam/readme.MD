# Terraform Hands-on Exam

This is a hands-on Exam in terraform, this exam came to check our understanding of basic usage of Terraform.
Parts 1 and 2 Contains a creation of VPC and EC2 instance, while Parts 3 and 4 emphasis on transferring Parts 1 and 2 into a module and build another module of an App Load Balancer.
(To organize the full assignment better i have uploaded the Terraform 20 Q&A and AWS .pdf files to this repository - see pdf directory for all files)


## Directory Structure

- `mock/`: Contains mock files for testing purposes.
  - `mock.tf`: Mock variables ant Data blocks used for testing.

## Part 1 & 2

- `network.tf`: Holds the security group.
- `varibales.tf`: Holds all the used variables in parts 1 and 2.
- `outputs.tf`: Holds all the outputs for parts 1 and 2.
- `vm.tf`: Holds all the configuration for the EC2 instance.
- `vpc.tf`: Holds all the configuration for the VPC.

## Parts 3 & 4

- `modulePart/main.tf`: contains the module ec2_vpc and module app_alb
  - `modules/ec2_vpc
    - `modules/ec2_vpc/main.tf`: Holds the logic for the ec2_vpc module
    - `modules/ec2_vpc/outputs.tf`: Holds the outputs of the module
    - `modules/ec2_vpc/varibales.tf`: Holds the variables used for the module (see modules section for more)
  - `module/alb`
    - `modules/alb/main.tf`: Holds the logic for the alb module
    - `modules/alb/outputs.tf`: Holds the outputs of the module
    - `modules/alb/varibales.tf`: Holds the variables used for the module (see modules section for more)

## Part 5 

As it was not explained on whocih file we should do Part 5 i have created a paragraph explaining the ways i would approch for the task in a debug.pdf file inside the directory pdf. 

## Modules

As requested in the third part of the test, I used modules, and this is also to make it more readable, more understandable, and to save code duplication. The modules are located in the modules/ directory. Here is a brief overview of each module:

- **vpc_ec2 Module**: Creates a VPC with public and private subnets, an internet gateway, and route tables. It takes variables such as `vpc_cidr`,`subnet_cidr` (which is a map for private and public subnets) and more. Outputs include IDs, CIDR blocks, Instances IPs and more for VPC components. Deploys an EC2 instance within the VPC. It uses variables like `ami`, `instance_type`, `vm_name`, `public_ip`,`assign_public_ip` and more to configure the instance.

- **alb Module**: Provisions an Application Load Balancer (ALB) to distribute traffic to EC2 instances. It requires variables such as `instance_type`, `subnets`, `vpc_id`, `subnet_ids`, and more. It sets up the ALB, target group, and listener. This module emphasis on the usage of our other module and insert varibales from our existing VPC. The module depends on the ec2_vpc module.

## Workflow

1.  **Initialization**: Run `terraform init` to initialize the working directory and download the necessary providers and modules.
2.  **Planning**: Run `terraform plan` to see the changes that Terraform will make to your infrastructure.
3.  **Deployment**: Run `terraform apply` to apply the changes and create the infrastructure.
4.  **Outputs**: After the deployment, Terraform will display the output values defined in `output.tf`.
5.  When you are done, you can run `terraform destroy` to remove all the resources created by Terraform.
    **Note**: Make sure to set up your AWS credentials and region before running Terraform commands.

## Customization

When you plan and apply, it will ask for the varibales (vpc_cidr, instance_type, ami, assigen_public_ip, subnet_count, subnet_cidr). To insert given values you can use the bellow command (One is a mock given to you to insert and try and the other one is a template of the command for your use):

```bash
terraform apply \
  -var="vpc_cidr=10.0.0.0/16" \
  -var="instance_type=t2.micro" \
  -var="ami=ami-0e1bed4f06a3b463d" \
  -var="assign_public_ip=true" \
  -var="subnet_count=2" \
  -var='subnet_cidr={"public"=["10.0.1.0/24","10.0.2.0/24"],"private"=["10.0.3.0/24","10.0.4.0/24"]}'
```

or

```bash
terraform apply \
  -var="vpc_cidr=<YOUR_CIDR>" \
  -var="instance_type=<YOUR_INSTANCE_TYPE>" \
  -var="ami=<YOUR_AMI>" \
  -var="assign_public_ip=<BOOLEAN>" \
  -var="subnet_count=<NUMBER>" \
  -var='subnet_cidr={"public"=[YOUR_PUBLIC_SUBNETS],"private"=[YOUR_PRIVATE_SUBNETS]}'
```

A better approach would be to use or create a .tfvars file which contains all the varibales (an example):

```terraform
vpc_cidr         = "10.0.0.0/16"
instance_type    = "t2.micro"
ami              = "ami-0e1bed4f06a3b463d"
assign_public_ip = true
subnet_count     = 2
subnet_cidr = {
  public  = ["10.0.1.0/24", "10.0.2.0/24"]
  private = ["10.0.3.0/24", "10.0.4.0/24"]
}
```

After creating the .tfvars file use it the following way:

```bash
terraform apply -var-file="<YOUR_FILE_NAME>.tfvars"
```
