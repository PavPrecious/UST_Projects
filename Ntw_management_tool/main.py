#!/usr/bin/python3

#Create network management tool:
import os
from management import *


def main_menu():
	print("\nEnter 1 for Assign IP address")
	print("Enter 2 for Delete IP address")
	print("Enter 3 for Display IP address")
	print("Enter 4 for Display all interfaces")
	print("Enter 5 for Configure routing")
	print("Enter 6 for Turn On/Off interface")
	print("Enter 7 for Add ARP entry")
	print("Enter 8 for Delete ARP Entry")
	print("Enter 9 for Restart Network")
	print("Enter 10 for Change hostname")
	print("Enter 11 for Add DNS server entry")
	print("Enter 12 for Exit")
	
while True:
	main_menu()
	choice = int(input("Enter your choice : "))
	if choice == 1:
		assign_ip()
	elif choice == 2:
		del_ip()
	elif choice == 3:
		display_ip()
	elif choice == 4:
		display_interface()
	elif choice == 5:
		configure_routing()
	elif choice == 6:
		trun_on_off_interface()
	elif choice == 7:
		add_arp_entry()
	elif choice == 8:
		delete_arp()
	elif choice == 9:
		restart_nw()
	elif choice == 10:
		change_host()
	elif choice == 11:
		add_dns_server_entry()	

	elif choice == 12:
		break
	else:
		print("Invalid choice")
	
	
		
