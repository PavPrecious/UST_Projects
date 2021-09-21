import os
import json

def status_container():
	cmd='docker ps -a'
	os.system(cmd)
	
def dwl_new_img():
	#Download new Image
	new_image=input("Enter image name:")
	cmd=f'docker pull {new_image}'
	res = os.popen(cmd).read()
	print(res)
def run_container():
	#Run container
	image=input("Enter image name : ")
	container_name = input("Enter container name : ")
	cmd = f'docker run -- name {container_name} {image}'
	os.system(cmd)
	res=os.popen('docker ps -a').read()
	print(res)
def dlt_container():
	#delete container
	container_name = input("Enter container name : ")
	cmd=f'docker rm {container_name}'
	res = os.popen(cmd).read()
	print(res)
	print("Deleted")
def nw_details_container():
	#network details of container
	cmd = 'docker network inspect bridge'
	l = os.popen(cmd).read()
	l = json.loads(l)[0]
	for i in l["Containers"].values():
		f'name => {i["Name"]} | Mac address => {i["MacAddress"]} | ipv4=>{i["IPv4Address"]}'
		
def mod_nw_details_container():
	#modify network details of container
	container_name = input("Enter container name : ")
	cmd = f'docker network disconnect bridge {container_name}'
	res = os.popen(cmd).read()
	print(res)
	print("Disconnected  from bridge network")
	new=input("Enter new network")
	cmd2=f'docker network create -d bridge --subnet=192.168.1.0/24 {new}'
	res2 = os.popen(cmd2).read()
	print(res2)
	print("created new network")
	
	cmd3=f'docker network connect {new} {container_name}'
	res3 = os.popen(cmd3).read()
	print(res3)
	print("Connected to new network")
	
	
