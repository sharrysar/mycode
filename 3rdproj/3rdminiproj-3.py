#!/usr/bin/env python
# from https://github.com/csfeeser/Netmiko-Example-Code/blob/master/presentations/dfwcug/examples/case6_config_change/config_change.py
from netmiko import Netmiko
from getpass import getpass

# saving kwargs to nxos1 variable
nxos1 = {
    'host': 'nxos1.twb-tech.com', 
    'username': 'pyclass', 
    'password': getpass(), 
    'device_type': 'cisco_nxos',
}
# config command that will be run remotely
commands = [
    'logging history size 500'
]
#connecting to device
net_connect = Netmiko(**nxos1)
# empty line and finding device command prompt
print()
print(net_connect.find_prompt())
# changing history size remotely and saving the changes
output = net_connect.send_config_set(commands)
output += net_connect.send_command("copy run start")
# print the variable output and an empty line
print(output)
print()