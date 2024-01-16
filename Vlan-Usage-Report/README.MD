
# Jdone VLAN USAGE REPORT

This tool has been created to automate information gathering process on vlan usage from any cisco devices.

'

![HOWTO](https://github.com/jdmg412/Uns3cure-Tools/blob/main/brute-tool/howto-BruteTool.JPG?raw=true)


## USAGE


First we need to install the requirements

```bash
pip install -r requirements.txt 
```

In order to use this tool once executed you need to provide credentials and destination host on the requested lines of the code, 
- (Replace default information with the ones you need), in the following format:

```bash
"host": "192.168.1.5", 
"username": "user", 
"password": "password", 
```

After saving you just need to run the code and enjoy.
```bash
python vlan-report.py
```


- Finally an xlsx file will be created with all the information you need to report.

```bash
username
```



