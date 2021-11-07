import hashlib
import os
import sys
import time
from termcolor import colored

golo = '''
            dP.         ____   __ _  _ _  _ ____    __ _
           88  ~;      |  __| /  | \/ | || |  _ \  /  | |
    ,ooooo888ooodbooo  |__  |/   |    | || |  _ < /   | |
    Y88888888888P"""   |____/_/|_|_||_|____|_| \_/_/|_|_|
         "888P            
      ,   "8P_____d8b    	HASH CRACKER
      'b ,ooP"""  Y88b,  	    By
       88P   ____  8881  	  EmreKybs
       888 """"""  888
       888b ~"Y8888888          
       Y888b      ,888
        "Y8888888b"88P
    _____,,,,,,,,,,,,,,______
ooo888P""""~~~~~~~~~~""""""Y88888
 "Y88"    ,do.  ""Y888b.
   ~    ,d8888     "Y888b
------------------------------------------------
https://github.com/emrekybs  
------------------------------------------------                                                                     
                                                      '''
print(golo)
time.sleep(1)
print("SAMURAI Starting ! ! !")
time.sleep(1.4)
supported_hashes = '''
\n
     (Hash Types)
        MD5
        SHA-1
        SHA-256
        SHA-512
\n
'''
print(colored(supported_hashes, 'red'))

if len(sys.argv) != 4:
    print(colored("[*]Usage python3 samurai.py <hash-value> <hash-type> <path-to-password-file>\n", 'white', attrs=['reverse', 'blink']))
    sys.exit(0)

hash_value = sys.argv[1]
hash_type = sys.argv[2]
pass_file = sys.argv[3]

if os.path.exists(pass_file) == False:
    print(colored("[!]Password File Not Found...exiting now", "red", attrs=['bold']))
    sys.exit(0)

with open(pass_file, 'r') as file:
    for line in file.readlines():
        
        if hash_type == 'md5':
            
            hash_object = hashlib.md5(line.strip().encode())
            hashed = hash_object.hexdigest()
            if hashed == hash_value:
            
                print("[*]Initializing Samurai. . . . .")
                print(colored(f"\n\n[+]MD5 Hash Cracked Successfully------Found = {line.strip()}\n\n", 'green', attrs=['bold']))
                sys.exit(0)

        elif hash_type == 'sha1':
           
            hash_object = hashlib.sha1(line.strip().encode())
            hashed = hash_object.hexdigest()
            if hashed == hash_value:
               
                print("[*]Initializing Samurai. . . . .")
                print(colored(f"\n\n[+]SHA-1 Hash Cracked Successfully------Found = {line.strip()}\n\n", 'green', attrs=['bold']))
                sys.exit(0)
        
        elif hash_type == 'sha256':
            
            hash_object = hashlib.sha256(line.strip().encode())
            hashed = hash_object.hexdigest()
            if hashed == hash_value:
              
                print("[*]Initializing Samurai. . . . .")
                print(colored(f"\n\n[+]SHA-256 Hash Cracked Successfully------Found = {line.strip()}\n\n", 'green', attrs=['bold']))
                sys.exit(0)

        elif hash_type == 'sha512':
            
            hash_object = hashlib.sha512(line.strip().encode())
            hashed = hash_object.hexdigest()
            if hashed == hash_value:
                
                print("[*]Initializing Samurai. . . . .")
                print(colored(f"\n\n[+]SHA-512 Hash Cracked Successfully------Found = {line.strip()}\n\n", 'green', attrs=['bold']))
                sys.exit(0)
        
    print(colored("\n[*]Please Consider Changing your wordlist of passwords\n", 'red', attrs=['bold']))
    print(print(colored("\n\n[!]Incorrect or Unsupported Hash Type or Password Not Found \n\n", 'red', attrs=['bold'])))
    print(print(colored("\n[*]Please Recheck the arguments you gave\n", 'red', attrs=['bold'])))
    sys.exit(0)
    
    
