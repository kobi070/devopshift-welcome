from dataclasses import dataclass, field

@dataclass
class Config:
    """
    ## Config Class:
        - Prompts the user for:
            - AMI choice: Ubuntu or Amazon Linux
            - Instance Type: t3.small or t3.medium
            - Region (only us-east-1 is allowed)
            - Load Balancer Name (custom input)
        - Returns:
            - Dict containing:
                - ami
                - instance_type
                - region (always 'us-east-1')
                - availability_zone_1
                - availability_zone_2
                - load_balancer_name
    """
    # Default values
    VALID_AMI: dict = field(default_factory=lambda: {"ubuntu": "ami-0c518311db5640eff", "amazon": "ami-0c518311db5640eff"})
    VALID_INSTANCE_TYPES: list = field(default_factory=lambda: ["t3.small", "t3.medium"])
    DEFAULT_REGION: str = "us-east-1"

    #  Varibales
    ami: str = field(init=False)
    instance_type: str = field(init=False)
    region: str = field(default=DEFAULT_REGION, init=False)
    availability_zone_1: str = field(init=False)
    availability_zone_2: str = field(init=False)
    load_balancer_name: str = field(init=False)

    def __post_init__(self):
        self.ami = self.get_ami()
        self.instance_type = self.get_instance_type()
        self.region = self.get_region()
        self.availability_zone_1 = f"{self.region}a"
        self.availability_zone_2 = f"{self.region}b"
        self.load_balancer_name = self.get_load_balancer_name()

    def get_ami(self) -> str:
        num_ami_choice = input("Please enter your AMI choice:\n1.Ubuntu\n2.Amazon\nChoice: ")
        ami_choice_list = list(self.VALID_AMI.keys())
        ami_choice = ami_choice_list[int(num_ami_choice)]
        return self.VALID_AMI.get(ami_choice, self.VALID_AMI["ubuntu"])  # Default to Ubuntu AMI

    def get_instance_type(self) -> str:
        num_instance_type_choice  = input("Enter your instance type:\n1.t3.small\n2.t3.medium\nChoice: ")
        instance_type_choice = self.VALID_INSTANCE_TYPES[int(num_instance_type_choice) - 1]
        return instance_type_choice if instance_type_choice in self.VALID_INSTANCE_TYPES else "t3.small"

    def get_region(self) -> str:
        region_choice = input("Enter your AWS region (only 'us-east-1' is allowed): ").strip().lower()
        if region_choice != self.DEFAULT_REGION:
            print(f"Invalid region '{region_choice}', defaulting to {self.DEFAULT_REGION}.")
        return self.DEFAULT_REGION  # Always default to 'us-east-1'

    def get_load_balancer_name(self) -> str:
        return input("Please enter Load Balancer name: ").strip()

    def to_dict(self) -> dict:
        return {
            "ami": self.ami,
            "instance_type": self.instance_type,
            "region": self.region,
            "availability_zone_1": self.availability_zone_1,
            "availability_zone_2": self.availability_zone_2,
            "load_balancer_name": self.load_balancer_name
        }

# Example usage
if __name__ == "__main__":
    config = Config()
    print(config.to_dict())
