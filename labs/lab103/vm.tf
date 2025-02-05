# Create a new resource using aws_instance named vm
# use the following var's to configurate the vm: ami, instance_type, vpc_security_group, tags
# run the user_data to add a new user

resource "aws_instance" "vm" {
 ami                         = data.aws_ami.terraformami.id
 instance_type               = var.vm_size
 vpc_security_group_ids      = [aws_security_group.sg.id]

 tags = {
   Name = var.vm_name
 }

 user_data = <<-EOF
   #cloud-config
   users:
     - name: ${var.admin_username}
       groups: sudo
       shell: /bin/bash
       sudo: ["ALL=(ALL) NOPASSWD:ALL"]
       lock_passwd: false
       passwd: $(echo ${var.admin_password} | openssl passwd -6 -stdin)
   EOF

 }

# Create a new output named vm_public_ip to show the new instance public_ip
output "vm_public_ip" {
 value = aws_instance.vm.public_ip
}