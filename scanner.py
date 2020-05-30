#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import socket
from datetime import datetime
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print ('invalid amount of argument')
    print ('Syntax:python scanner.py <ip>')

print ('#' * 50)
print ('-' * 50)
print ('Scanning Target' + target)
print ('Time Started' + str(datetime.now()))
print ('-' * 50)
print ('#' * 50)
try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = s.connect_ex((target, port))
        if result == 0:
            print ('port  ' +  str(port)  + '  is open')
        s.close()
except KeyboardInterrupt:
    print ('Exiting Program')
    sys.exit()
except socket.gaierror:
    print ("hostname couldn't be resolved")
    sys.exit()
except socket.error:
    print ("couldn't connect to the server")
    sys.exit()
