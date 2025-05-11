###Ping or Scan for Open Ports###
import os, time #needed libraries

os.system("clear") #just to clear terminal


def pinging():
    host = input("what is the name of the host that you are trying to ping? ".title())
    quantity = int(input("how many times do you want me to ping ".title() + host + "? "))
    
    print("okay, i will begin to ping".title(), host, "in 5 seconds...".title())
    for i in range(5, 0, -1):
        time.sleep(1)
        print(i, end=" ", flush=True)
    time.sleep(1)
    os.system(f"ping {host} -c {quantity}")

def scanning():
    host = input("Please enter a host that you want to scan for open ports: ")
    print("Okay, I will begin the scan in 5 seconds...")
    for i in range(5, 0, -1):
        time.sleep(1)
        print(i, end=" ", flush=True)
    os.system("clear")
    os.system(f"nmap {host} -vv -Pn")

option = int(input("please choose an option (ping a host [1], or scan host for open ports [2]): ".title()))
if option == 1:
    pinging()
elif option == 2:
    scanning()
else:
    print("That is not a valid option!")
