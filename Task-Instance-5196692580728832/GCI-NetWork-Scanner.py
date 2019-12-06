import socket
import subprocess
from datetime import datetime as dt

user_ip = socket.gethostbyname(socket.gethostname())
ip = user_ip.split('.')
print("==========Script By UTx10101===========")

ip_start = ("%s.%s.%s." %(ip[0],ip[1],ip[2]))
t1 = dt.now()

def Run():
	k=0
	l=0
	print("Scanning Network :",ip_start+"0\n")
	rng = input("Enter a range to scan (Eg: start - end): ")
	for ip in range(int(rng.split("-")[0].strip()),int(rng.split("-")[-1].strip())+1):
		addr = ip_start + str(ip)
		res = subprocess.call(['ping', '-c', '3', addr])
		if (res==0):
			k+=1
			print("Device Found on: ", addr)
		elif(res==2):
			l+=1
			print("No Response from: ", addr)
	return k,l
K,L=Run()
print("==================Script-Output==================")
print("\n%d Devices Found on Network" %(K+L))
print("Live: %d		Not Live: %d" %(K,L))
t2 = dt.now()
total = t2 - t1
print("Total Time Taken: " , total)
print("\n=================================================")
