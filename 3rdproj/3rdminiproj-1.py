#!/usr/bin/env python

# from https://github.com/csfeeser/Netmiko-Example-Code/blob/master/presentations/dfwcug/examples/case2_using_dict/conn_with_dict.py

# importing modules
from netmiko import Netmiko
from getpass import getpass

# saving router(?) info on variable 'cisco1' to pass down in line 17
cisco1 = {
    'host': 'cisco1.twb-tech.com', 
    'username': 'pyclass', 
    'password': getpass(), 
    'device_type': 'cisco_ios',
}

# creates an object based on device type
net_connect = Netmiko(**cisco1)
# finds the current network device prompt
print(net_connect.find_prompt())
# close the session
net_connect.disconnect()