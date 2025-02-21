from utils.config import Config
from terraform.exec_terraform import TerraformManager
from aws.aws_validator import AWSValidator
from utils.logger import setup_logging

# Initialize logger
logger = setup_logging()

def main():
    # Initialize Config, TerraformExecutor, and AWSValidator
    config = Config()
    terraform = TerraformManager(config)

    logger.info("Generating Terraform script...")
    # Generate the Terraform configuration based on the config
    terraform.generate_terraform()

    logger.info("Executing Terraform...")
    terraform_output = terraform.apply_terraform("generated/main.tf")
    
    if not terraform_output:
        logger.error("Terraform deployment failed!")
        return

    # Get values like instance ID and load balancer name from the output or config
    instance_id = terraform_output.get("instance_id", "extracted-instance-id")  # Adjust as necessary
    alb_name = config.load_balancer_name
    validator = AWSValidator(instance_id=instance_id, alb_name=alb_name)

    logger.info("Validating AWS Deployment...")
    # Validate the EC2 instance and load balancer using the AWSValidator
    ec2_data = validator.validate_instance(instance_id)
    alb_data = validator.validate_alb(alb_name)

    if ec2_data and alb_data:
        validation_data = {**ec2_data, **alb_data}
        validator.save_validation(validation_data)
        logger.info("AWS validation successful!")
    else:
        logger.error("AWS validation failed!")

if __name__ == "__main__":
    main()
