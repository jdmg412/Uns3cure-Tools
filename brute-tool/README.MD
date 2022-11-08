
============================================================================================
[+]Welcome to Uns3cure brute force login, this tool has been created for PoC purposes only 
by proving weak credentials on bussineses web services using a wordlist or list of sql-payloads.
===============================================================================================
'

![HOWTO](https://github.com/jdmg412/Uns3cure-Tools/blob/main/brute-tool/howto-BruteTool.JPG?raw=true)

===============
    USAGE

#[+]First we need to install the requirements\n
pip install -r requirements.txt 


#[+]In order to use this tool once executed you need to provide a url, 
#(try with the one that is used for POST on the requests found under the inspect mode of your browser) in the following format:\n
https://example.com/login.php


#[+]Next you will need to provide a username for the bruteforce attack
Admin


#[+]Provide the field name that is use for the username durning the POST request
(you can find this information using burpsuit or inspecting the POST request on your browser under /netwok/request)
username


#[+]Provide the field name that is use for the password durning the POST request(find it where you found de user field values)
password


#[+]In case there's more field values for de POST requests than default you might need to change de payload values in brute-tool.py
payload = {'<field>':'<value>', ufield:user, pfield:line}

    
#[+]In case you want to use another word/sql-payloads list other than default like "Rockyou.txt" change de file in brute-tool.py 
#(***add something like "ksdj" in the first line of the list to generate an intentional fail login***)
with open("<file-path>") as f:


======================================================
You can test this in https://demo.testfire.net/doLogin
======================================================


----------END-------------

