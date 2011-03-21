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

server = "citrussummer"
client = nfs4lib.NFS4Client("bla" , server, homedir = ["/fs/1"])
print client.getLeaseTime()
print client.go_home()
#print client.do_getfh("/fs/1/a")
print client.do_getattr(nfs4_const.FATTR4_FS_LOCATIONS,"a")
