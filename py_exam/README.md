# DevOps Shift Welcome
Welcome to the DevOps Shift project! This repository contains various scripts, configurations, and examples to help you get started with DevOps practices using Python, Terraform, and other tools.
## Directory Structure
devopshift-welcome/
- .gitignore
- .vscode/
    -  launch.json
- code/
    - samples/
    - solutions/
- credentials.txt
- docker-demo/
    - app/
    -  Dockerfile
- exam/
    - .terraform/
    - .terraform.lock.hcl
    - mock/
    - modulePart/
    - terraform.tfstate
    -  terraform.tfstate.backup
- generatessh-agent.sh
- py_exam/
    - aws/
    - generated/
    - logs.json
    - main.py
    - terraform/
    -  utils/
- py_labs/
    - lab101/
    - lab102/
    - lab103/
    - lab104/
    -  lab105/
- python/
    - assigment.py
    - classes-demo.py
    - cloud.py
    - dataclasses-demo.py
    - files-demo.py
    - fn-demo.py
    - json-demo.py
    - jsonformatter.py
    - lg.py
    - req-demo.py
    - request-dm.py
    - servers.txt
    -  subproc-demo.py

## Getting Started
### Prerequisites
 - Python 3.10 or higher
 - Terraform
 - AWS CLI configured with appropriate credentials

### Installation
Clone the repository:
```bash
git clone <repository-url>
cd devopshift-welcome
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```
### Usage
The py_exam/terraform/ directory contains Terraform scripts for deploying AWS resources.
To generate and apply a Terraform configuration, run the main.py script in the py_exam/ directory:
```bash
python py_exam/main.py
```


License
This project is licensed under the MIT License.

Contact
For any questions or issues, please open an issue in the repository.

Happy DevOps-ing! 🚀