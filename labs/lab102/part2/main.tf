
variable "public_ip" {
  default = "10.20.30.40"
  description = "Mock Data to check if a certain public_ip is created or not"
}

# Will use aws_instance.vm.public_ip in lab102 as this is only mock data
resource "null_resource" "check_public_ip" {
  provisioner "local-exec" {
    command = <<EOT
      if [ -z "${var.public_ip}" ]; then
        echo "ERROR: Public IP address was not assigned." >&2
        exit 1
      fi
    EOT
  }

# For production in main lab102 not in the mock
#   depends_on = [aws_instance.vm]
}

# Will use aws_instance.vm.public_ip in lab102 as this is only mock data
output "vm_public_ip" {
  value      = var.public_ip
  depends_on = [null_resource.check_public_ip]
  description = "Mock Test Public IP address of the VM"
}