#! /usr/bin/python3

import os

response = input(" what will you like to do \n 1. Add a new network adapter \n 2. Remove an existing network adapter \n Please enter the number ::")
if (response == "1"):

    os.system("modprobe dummy")
    network_name= input("Enter your preffered network name (e.g. eth1) \n ::")
    network_num= input("Please Enter the number after your network name (e.g.1) \n ::")

    os.system("ip link add " + network_name + " type dummy")
    os.system("ip link show " + network_name)

    network_mac = input("Enter network mac address (e.g. 00:d5:3t:2r:ss:3t) \n ::")

    os.system("ifconfig " + network_name +" hw ether " + network_mac)

    network_ip = input("Enter network ip address (e.g. 192.168.1.2/24) \n ::")

    os.system("ip addr add " + network_ip + " brd + dev " + network_name + " label " + network_name +":" + network_num )
    os.system("ip link set dev " + network_name +" up")

    #x = os.system("ip a")
    print("Network adapter added successfully.")

elif(response == "2"):
    network_name= input("Enter the network name you choose to remove (e.g. eth1) \n ::")
    network_num= input("Please Enter the number after your network name (e.g.1) \n ::")
    network_ip = input("Please Enter "+ network_name + "'s ip address (e.g. 192.168.1.2/24) \n ::")
    os.system("ip addr del " + network_ip + " brd + dev " + network_name + " label " + network_name +":" + network_num )
    os.system("rmmod dummy")
    print("Network adapter removed successfully.")