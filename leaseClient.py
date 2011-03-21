#!/usr/bin/env python

#                    Information Technology Integration
#

import sys
import os
# Allow to be run stright from package root
if  __name__ == "__main__":
    if os.path.isfile(os.path.join(sys.path[0], 'lib', 'testmod.py')):
        sys.path.insert(1, os.path.join(sys.path[0], 'lib'))

import nfs4.nfs4lib as nfs4lib
import nfs4.nfs4_type as nfs4_type
import nfs4.nfs4_const as nfs4_const
import nfs4.nfs4_pack as nfs4_pack
import code
import traceback
import time
import string
import threading 

server = "servername"
THREADS = 15



def getLease():

	clients = []
	for i in range(0,10):
		s = ""
		for i in range(0,10): s += string.lowercase[ord(os.urandom(1)) % 26]
		print s
		client = nfs4lib.NFS4Client(s , server, homedir = [])
		clients.append(client)
	i = 0
	while i < 30:
		time.sleep(1)
		for client in clients: print client.getLeaseTime()
		i+=1


def startThreads():
	threadDict = []
	for i in range(0,THREADS):
		th = threading.Thread(target = getLease)
		th.start()
		threadDict.append(th)

	for thread in threadDict:
		thread.join()

	th.join()
	print threading.active_count()


if os.fork() == 0:
	startThreads()
else:
	startThreads()









