from netmiko import ConnectHandler
import pandas as pd
import time
import sys
import re


z='''
=========================================
        *VLAN USAGE - REPORT PCI*
        -------------------------
          Ver 1.0  | Jose Done
=========================================
'''

for s in z:
    sys.stdout.write(s)
    sys.stdout.flush()
    time.sleep(0.02)

descriptions=[]
interfaces=[]
vlans=[]

#Connection Information
Network_Device = {"host": "192.168.1.5", 
                  "username": "user", 
                  "password": "password", 
                  "device_type": "cisco_ios"}

Connect = ConnectHandler(**Network_Device)
Connect.enable()

To_Issue = "sh int status | exclude disabled | trunk"


# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines((Connect.send_command(To_Issue, read_timeout=3600)))
file1.close()

# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()

count = 0
for line in Lines:
    count += 1
    linex = str(line.strip())

    interface = str(re.findall("Gi1/[0-1]/[0-9]", linex))
    interface2 = str(re.findall("Gi1/[0-1]/[0-9][0-9]", linex))
    
    if interface2 == "[]":
    
        temp = str(interface)
        interfaces.append(temp)

    else:
        temp2 = str(interface2)
        interfaces.append(temp2)


Interfaces2=[]



for i in range(0,len(interfaces)):
    if str(interfaces[i]) == "[]":
        print("Filtered")
    else:
        inter = str(interfaces[i])
        inter = inter.replace("['", "")
        inter = inter.replace("']", "")

        Interfaces2.append(inter)

        To_Issue2 = (f"sh run int {inter} | inc desc")
        To_Issue3 = (f"sh run int {inter} | inc vlan")

        print(inter)
        

        infile = Connect.send_command(To_Issue2, read_timeout=3600)
        print(infile)
        #writeIn(infile)
        infile = infile.replace("description", "")
        descriptions.append(str(infile))

        infile2 = Connect.send_command(To_Issue3, read_timeout=3600)
        print(infile2)
        infile2 = infile2.replace("switchport access", "")
        vlans.append(str(infile2))
        
#print(descriptions)
        


final=zip(Interfaces2, vlans, descriptions)
# convert into dataframe
df = pd.DataFrame(final)

#convert into excel
df.to_excel("report_vlan_usage.xlsx", index=False)

# All done hope it helps ;)
print("Dictionary converted into excel...")



