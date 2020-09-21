import sys
import socket
import random
import struct
import time
from subprocess import Popen, PIPE
from scapy.all import *
import shlex
import datetime
from variables import *


def main():
    print "waiting"
    while True:
        if datetime.datetime.now().strftime('%S') == '00':
            break
    print "running"
    timeout = 0.03
    cmd = "timeout 0.1 ping 10.0.0.2 -c 1"
    k = 0
    for i in range(message_length):
	start=time.time()
        print "Round" + str(k) + " is started at " + datetime.datetime.now().strftime('%H:%M:%S')
        k = k + 1
        time.sleep(delta_s + delta_r)
        output = Popen(cmd,stdout=PIPE,shell=True)
        response = output.communicate()[0]
        time.sleep(delta_p)
	stop=time.time()
	print "elapsed time" + str(stop-start)
if __name__ == '__main__':
    main()


