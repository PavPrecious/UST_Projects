#!/usr/bin/python3

#System Health
import os
from system_health import *

def main_menu():
	print("Please enter 1 for Display available RAM")
	print("Please enter 2 for Display Load average")
	print("Please enter 3 for Display Hostname details")
	print("Please enter 4 for Display All process count")
	print("Please enter 5 for Display uptime")
	print("Please enter 6 for Exit")
	
while True:
	main_menu()
	ch=int(input("Please enter your choice : "))
	if ch == 1:
		display_available_ram()
	elif ch == 2:
		display_load_avg()
	elif ch == 3:
		display_host_details()
	elif ch == 4:
		display_all_process_c()
	elif ch == 5:
		display_uptime()
	elif ch == 6:
		break
	else:
		print("Invalid choice")

