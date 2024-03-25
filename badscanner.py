import sys
import socket
from datetime import datetime

#Syntax: python3 badscanner.py <ip>

#Defining our target
if len(sys.argv) == 2:  #argv takes in the argument passed by the user.
    target = socket.gethostbyname(sys.argv[1])  #Translates hostname to IP address. argv[1] is the ip address.
else:
    print("""Invalid amount of arguments.
Syntax: python3 badscanner.py <ip>""")

#Adding a banner
print("-" * 50)
print("Scanning target: " +target)
print(f"Time started: {datetime.now()}")
print("-" * 50)

#Finding open ports
try:
    for port in range(20,445):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #Error method; if the port is open, the method returns '0', and if the port is closed, it returns '1'.
        if (result == 0):
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting program...")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()
