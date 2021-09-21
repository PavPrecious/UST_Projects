import os

def display_available_ram():
	#Display available RAM
	mem = os.popen('free -m').read()
	print("____memory details______")
	print(mem)
def display_load_avg():
	#Display Load average
	cmd = 'cat /proc/loadavg'
	res = os.popen(cmd).read()
	print(res)
def display_host_details():
	#Display Hostname details
	cmd = 'hostnamectl status'
	res = os.popen(cmd).read()
	print(res)
def display_all_process_c():
	#Display All process count
	cmd = 'ps -a | wc -l'
	res = os.popen(cmd).read()
	print(f' Process count =>{res} ')
def display_uptime():
	#Display uptime
	cmd = 'uptime -s'
	res = os.popen(cmd).read()
	print(res)
