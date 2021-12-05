import hashlib


K = '\033[93m'
U = '\033[95m'
C = '\033[94m'
R = '\033[91m'
H = '\033[92m'

flag = 0
counter  = 0



print
print (U+"                                                            version:1.0")
print (K+"===========================================================")
print (R+"Author         : Mr.Noname")
print (H+"Github Us      : https://github.com/PanocTeam25")
print (H+"Team           : Pancasila anonim cyber")
print (H+"Thanks         : All Member Panoc")
print (H+"Instagram      : Panoc.Team")
print (K+"===========================================================")
print


pass_hash = input("Enter md5 Hash: ")

wordlist = input("Nama File: ")

try:
    pass_file = open (wordlist, "r")
	except:
	print("File Tidak Ditemukan Cok")
	quit()
	
for word in pass_file:

enc_wrd = word.encode('utf-8')
digest = hashlib.md5(enc_wrd.strip()).hexdigest()

#   print(word)
#   print(digest)
#   print(pass_hash)
counter += 1

if digest == pass_hash:
    print("Password Ditemukan")
	print("Passwornya Adalah " + word)
	flag = 1
	break
	
	if flag == 0:
	print("password/passphrase is not in the list")