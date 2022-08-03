#!/usr/bin/python3

ipchk = input("Apply an IP address: ")


if ipchk == "192.168.70.1":
    print("Looks like the IP address of the Gateway was set: " + ipchk + ". This is not recommended ")
elif ipchk:
    print("Looks like the IP addrest was set: " + ipchk)
else:
    print("Please provide an input")
