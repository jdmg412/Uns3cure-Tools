import re
import sys
import time
import requests
import requests.exceptions
from bs4 import BeautifulSoup, Comment
from colorama import Fore, Back, Style
import termcolor
import os


os.system('color')

z = '''
============================================

        WEB SCRAPER - HIDDEN COMMENTS
        -----------------------------
                By Uns3cure

===========================================

'''
for l in z:
    sys.stdout.write(termcolor.colored(l, 'green'))
    sys.stdout.flush()
    time.sleep(0.02)


url = input("provide URL to scrape: ")

#url = "https://demo.testfire.net"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

archive_links = []
junk = []

def start_letter(string):
    return bool(re.match(r'[a-zA-Z]', string))

def start_sign(string):
    return bool(re.match(r"[a-z]+#", string))

for a_href in soup.find_all("a", href=True): 
    #print(a_href["href"])
    i = str(a_href["href"])


    if i[0] == "m":
        junk.append(i)

    elif i[0] == "h":
        archive_links.append(i)
        #print(i)
    
    elif i[0] == "/":
        #print(url + i)
        archive_links.append(url + i)

    else:
        junk.append(i)


for link in archive_links:
        try:
            page2 = requests.get(link)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue
        print("================================================================")
        print(termcolor.colored(link, 'blue'))
        print("================================================================")
        soup2 = BeautifulSoup(page2.content, "html.parser")


        for comment in soup2.findAll(text=lambda text:isinstance(text,Comment)):
            #print(link)
            print(termcolor.colored(comment, 'green'))

print(archive_links)
 



    

print("======Finished!======")
exit()
                    



