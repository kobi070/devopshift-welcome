provider "azurerm" {
  features {}
  subscription_id="3f79a68d-cf0d-4291-a31f-185897f7fda1"
}


data "azurerm_network_interface" "oleg_nic" {
  name                = "oleg-nic"
  resource_group_name = "oleg-terraform-rg"
}

output "whole_data" {
  value = data.azurerm_network_interface.oleg_nic
}