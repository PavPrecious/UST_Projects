import MySQLdb as mysql
from rich.prompt import Prompt
from rich import style
from rich.console import Console
from rich import style
import pprint
import time
import json


console = Console()
db = mysql.connect(host='localhost', user='root', password='1234', db="INFORMATION_SCHEMA")
cur = db.cursor()
cur.execute('SHOW STATUS')
res = cur.fetchall()
r = dict(res)
pprint.pprint(r)

def Info_of_Database():
	console.print(f"Uptime, {r['Uptime']}", style='bold magenta')
	console.print(f"Threads_created, {r['Threads_created']}", style='bold magenta')
	console.print(f"Threads_connected, {r['Threads_connected']}", style='bold magenta')
	console.print(f"Threads_running, {r['Threads_running']}", style='bold magenta')
	console.print(f"Queries, {r['Queries']}", style='bold magenta')
	console.print(f"Max_used_connections, {r['Max_used_connections']}", style='bold magenta')

def Show_the_process_list():
	cur.execute("select ID,DB from PROCESSLIST") 
	res = cur.fetchall()
	console.print(res)

def Exit():
	exit()
	
def main_menu():
	console.print("1.Information Of Database",style="bold cyan")
	console.print("2.Show Process List",style="bold cyan")
	console.print("3.Exit",style="bold cyan")
	
operations = {
    "1":Info_of_Database,
    "2":Show_the_process_list,
    "3":Exit
}

while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()
	
cur.close()

