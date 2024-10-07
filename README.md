# port-scanner code explained

import sys
import socket
from datetime import datetime

#now lets define our target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
#this going to translate hostnames to ipv4
else:
       print("invalid amount of argument")
       print("syntax: python3 scanner.py ,ip.")

#we are taking a method of length and we are saying sys.argv(its the amount of argument that we are giving

#so we need to have 2 arguments if we have 3 its going to break...if we have one its going to break

#as if we were saying :

#python 3 scanner.py 192.168.1.10 4444
#its going to break

#if it does meet the length we are going to set our target to socket.gethostbyname ....and the [1] its an argument of ip add

#now lets add a pretty banner
print("*" * 50)
print("scanning target: "+target)
print("time started: "+str(datetime.now()))
print("*" * 50)

#now lets try the for loop for ports

try:
       for port in range(50,85):
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               socket.setdefaulttimeout(1)
#if it dosnt respond back within 1 sec we gonna move back
               result = s.connect_ex((target,port))
               if result == 0:
                   print(f"port {port} is open ")

               s.close()
#we did a for loop dor ports from 50 to 85

#we set a variable s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#we are going to gather the ipv4 through AF_INET is = to ipv4
#and the port we are going to connect to through socket.SOCK_STREAM)

#target is going to be supplyed by us and the port in range 50-85
#if a port is open the result is 0
#if not the sockr=et connection close and goin back to the loop

except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()
#if we hit ctrl C
except socket.gaierror:
    print("host name could not be resolved")
    sys.exit()

except socket.error:
    print("could not connect to the server")
    sys.exit()

#if the server doesn't respond back

# whats next ?

1-save this as a python file
2-you shall be locating your directory where you saved your python file and open it with your cmd or pycharm terminal
3-and type this for example
python3 port-scanner.py 192.168.10.1 (for example ...you can type the ip you prefer)
