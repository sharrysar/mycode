#!/usr/bin/env python
# from https://github.com/csfeeser/Netmiko-Example-Code/blob/master/presentations/dfwcug/examples/case9_ssh_keys/conn_ssh_keys.py

# importing modules
from netmiko import Netmiko
from getpass import getpass

# variable that contains user's private key
key_file = "/home/gituser/.ssh/test_rsa"

# router(?) info saved in cisco1 variable
cisco1 = {
    'device_type': 'cisco_ios',
    'host': 'cisco1.twb-tech.com', 
    'username': 'testuser',
    'use_keys': True,
    'key_file': key_file,
}

# passing cisco1 info in netmmiko function to connect
net_connect = Netmiko(**cisco1)
# finds the current network device prompt
print(net_connect.find_prompt())
# running a command remotely: router's arp
output = net_connect.send_command("show ip arp")
# print the output of the command
print(output)