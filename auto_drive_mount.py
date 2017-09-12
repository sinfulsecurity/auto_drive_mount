"""
Script: auto_drive_mount.py
Author: Dennis (DJ) Moder
Disclosure: Script was developed on my personal time, with personal assets. This script is free to use
and free to modify.
License: GNU General Public License
Script Purpose: Allows for interactive mounting of remote drives and cuts back on the monotonous net use commands
"""


import getpass
import subprocess

Target = raw_input("What input the target hostname: ")
User = raw_input("Please input your username: ")
Pass = getpass.getpass()
Drive = raw_input("Please enter a drive letter: ")


print ("[!] Dismounting specified drive, just in case.")
#Dismounts specified drive letter, just in case :)
subprocess.call(r'net use '+Drive+' /del', shell=True)


print ("[!] Connecting to Hostname")
# Connect to shared drive, use drive letter M
subprocess.call(r'net use ' + Drive+':' + r' \\'+Target+'\c$' + ' '+'/user:'+User+' '+Pass, shell=True)

print ("[*] Process Complete. Please confirm drive mounted successfully")
