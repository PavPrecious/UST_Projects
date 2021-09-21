#!/usr/bin/python3

import os
import json
from manage_docker import *
	
def main_menu():	
	print("Enter 1 for Status of containers")
	print("Enter 2 for Download new Image")
	print("Enter 3 for Run container")
	print("Enter 4 for Delete Container")
	print("Enter 5 for Network details of container")
	print("Enter 6 for Modify Network details of contaniner")
	print("Enter 7 for Exit")
	
	
while True:
	main_menu()
	ch = int(input("Enter your choice : "))
	if ch == 1:
		status_container()
	elif ch == 2:
		dwl_new_img()
	elif ch == 3:
		run_container()
	elif ch == 4:
		dlt_container()
	elif ch == 5:
		nw_details_container()
	elif ch == 6:
		mod_nw_details_container()
	elif ch == 7:
		break
	else:
		print("Invalid choice")
