#!/usr/bin/python
#coding: utf-8

import hashlib
import os 

os.system("clear")
flag = 0

print("\033[1;32;40m ░░░░░██╗░█████╗░██╗░░██╗███████╗██████╗░  ██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░")
print("\033[1;32;40m ░░░░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗  ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗")
print("\033[1;32;40m ░░░░░██║██║░░██║█████═╝░█████╗░░██████╔╝  ███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝")
print("\033[1;32;40m ██╗░░██║██║░░██║██╔═██╗░██╔══╝░░██╔══██╗  ██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗")
print("\033[1;32;40m ╚█████╔╝╚█████╔╝██║░╚██╗███████╗██║░░██║  ██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║")
print("\033[1;32;40m ░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝\n")
print("                            This Script Was Made By JOKER HACKER​​​​​                          ")
 
                                                                                                                                   
pass_hash = input("\033[1;36;40m Enter the md5 hash: ")
wordlist = input("\033[1;36;40m  Wordlis Location: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print("\tpassword found")
        print("Password is " + word)
        flag = 1
        break

if flag ==0:
    print("\tPassword is not in the list")
