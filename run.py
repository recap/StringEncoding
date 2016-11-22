import sys
import struct
import re
import os

from StringEncoding import *


myEncoding = StringEncoding()

bytes = sys.stdin.read()
x = bytes[:-1].decode("hex")
d = bytearray(x)
l = myEncoding.decode(d)
k = os.getenv("USE_TRIVIAL_IMPLEMENTATION", 0)
if(int(k) ==  1):
	r = myEncoding.encode(l,True)
else:
	r = myEncoding.encode(l,False)
	

sys.stdout.write("stdout: " +l+"\n")
sys.stderr.write("stderr: "+str(r)+"\n")

