provider "azurerm" {
  features {}
  subscription_id="3f79a68d-cf0d-4291-a31f-185897f7fda1"
}

# Defines our variables
# Name Var
variable "name" {
  default = "kobi"
}

# Define your SSH public key
variable "ssh_public_key" {
  default = "~/.ssh/id_rsa.pub"
}

data "azurerm_network_interface" "oleg_nic" {
  name                = "oleg-nic"
  resource_group_name = "oleg-terraform-rg"
}

variable "nw_inf_id" {
  default = "/subscriptions/3f79a68d-cf0d-4291-a31f-185897f7fda1/resourceGroups/oleg-terraform-rg/providers/Microsoft.Network/networkInterfaces/oleg-nic"
}


# Create a small Linux VM
resource "azurerm_linux_virtual_machine" "vm" {
  name                  = "${var.name}-vm"
  location              = data.azurerm_network_interface.oleg_nic.location
  resource_group_name   = "oleg-terraform-rg"
  network_interface_ids = [var.nw_inf_id]
  size                  = "Standard_B1s" # Small instance size

  os_disk {
    name                 = "${var.name}-os-disk"
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  admin_username = "azureuser"
  admin_ssh_key {
    username   = "azureuser"
    public_key = file(var.ssh_public_key)
  }

  disable_password_authentication = true
}

output "name" {
  value = azurerm_linux_virtual_machine.vm.name
}

output "location" {
  value = azurerm_linux_virtual_machine.vm.location
}

output "ip_address" {
  value = azurerm_linux_virtual_machine.vm.public_ip_address
}

output "admin_ssh_key" {
  value = azurerm_linux_virtual_machine.vm.admin_ssh_key
}

output "zone" {
  value = azurerm_linux_virtual_machine.vm.zone
}