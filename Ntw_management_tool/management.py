import os

def assign_ip():
	#Assign IP address
	ip=input("Please enter ip address to assign : ")
	if len(ip.split('.')) == 4:
		interface = os.popen('ip l').read()
		print(interface)
		choice=input("Please enter interface : ") 
		cmd = f'ip address add {ip} dev {choice}'
		ip_assign = os.popen(cmd).read()
		print(ip_assign)
		print("Ip address assigned successfull")
def del_ip():
	#Delete IP address
	ip=input("Please enter ip address to delete : ")
	if len(ip.split('.')) == 4:
		interface = os.popen('ip l').read()
		print(interface)
		choice=input("Please enter interface : ") 
		cmd = f'ip address del {ip} dev {choice}'
		ip_del = os.popen(cmd).read()
		print(ip_del)
		print("Ip address deleted successfull")
def display_ip():
	#Display IP address
	cmd= f'ip -c -br address'
	res=os.popen(cmd).read()
	print(res)
def display_interface():
	#Display all interface
	cmd = 'ip l'
	res = os.popen(cmd).read()
	print("____Interface Details________")
	print(res)
	
def configure_routing():
	#Configure routing
	nw_addr = input("Please enter network address with mask(nw add/mask) : ")
	gate_way = input("Please enter gateway ip address : ") 
	if len(nw_addr.split('.')) == 4 and len(gate_way.split('.')) == 4:
		cmd = f'ip r add {nw_addr} via {gate_way}'
		res = os.popen(cmd).read()
		print(res)
		print("Sucessfull")
def trun_on_off_interface():
	#Turn On/Off interface
	print("Please enter 1 for Turn on interface")
	print("Please enter 2 for Turn off interface")
	ch = int(input("Please enter your choice : "))
	interface = os.popen('ip l').read()
	print(interface)
	choice=input("Please enter interface : ")
	if ch == 1:
		cmd = f'ip link set dev {choice} up'
		res = os.popen(cmd).read()
		print(f'{choice} turned on | Details :{res}')
	elif ch ==2:
		cmd = f'ip link set dev {choice} down'
		res = os.popen(cmd).read()
		print(f'{choice} turned off | Details :{res}')
	else:
		print("Invalid")
		
def add_arp_entry():
	#Add ARP entry
	ip=input("Please enter ip address to assign : ")
	if len(ip.split('.')) == 4:
		interface = os.popen('ip l').read()
		print(interface)
		choice=input("Please enter interface : ")
		arp_cache = os.popen('ip n show | cut -d " " -f5').read()
		cmd=f'ip n add {ip} lladdr {arp_cache} dev {choice} nud permanent'
		res = os.popen(cmd).read()
		print("arp entry added ")

		
def delete_arp():
	#Delete ARP Entry
	ip = input('Please enter ip address : ')
	if len(ip.split('.')) == 4:
        	interface = os.popen('ip l').read()
        	print(interface)
        	choice = input("Please enter interface : ")
        	cmd = f'ip n del {ip} dev {choice}'
        	res = os.popen(cmd).read()
        	console.print('ARP Entry deleted successfully ')
def restart_nw():
	#Restart Network
	cmd = 'sudo systemctl restart networking'
	cmd2 = 'sudo systemctl status networking'
	os.popen(cmd).read()
	print('Network services restarted ')
	print(os.popen(cmd2).read())
def change_host():
	#Change hostname
	host_name = input("Please enter new host name :")
	cmd = f'hostnamectl set-hostname {host_name}'
	os.popen(cmd).read()
	print(f'new host name {host_name} set successfully ')
def add_dns_server_entry():
	#Add DNS server entry
	print('adding dns server')
	print('first : nameserver 8.8.8.8 write in this format')
	print('second : ctrl + d  to exit ')
	cmd = 'sudo cat  >> /etc/resolv.conf'
	print(os.popen(cmd).read())
	print('Added successfully  ')
