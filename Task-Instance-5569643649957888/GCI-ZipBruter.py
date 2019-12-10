import zipfile
from datetime import datetime as dt

zfile=input("\nEnter Name or Location of ZipFile to be cracked: ")
wlist=input("Enter Name or Location of Wordlist: ")

passwd=None

zFile=zipfile.ZipFile(zfile)
t=dt.now()
flg=1
with open(wlist, 'r') as wl:
	for l in wl.readlines():
		passwd=l.strip('\n')
		try:
			zFile.extractall(pwd=passwd.encode())
			print("\n		Found Password for %s:  %s" %(zfile,passwd))
			print("		Total Time Taken: ",dt.now()-t,"\n")
			flg=0
			break
		except:
			continue
if(flg):
	print("\n\n		Couldn't Find Password for %s:  %s" %(zfile,passwd))
	print("\n		Total Time Taken: ",dt.now()-t)
