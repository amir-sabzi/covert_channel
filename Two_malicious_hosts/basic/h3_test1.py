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
    cmd = "nping --source-mac 00:00:00:00:00:01 -S 10.0.0.1 10.0.0.2 -c 1"
    intervals=[]
    for i in range(sample_num):
        phase1_start=time.time()
        print "Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S')
        output = Popen(cmd,stdout=PIPE,shell=True)
        response = output.communicate()[0]
        phase1_finish=time.time()
        phase1_delay = phase1_finish - phase1_start
        time.sleep(delta_1 + delta_2 + delta_3 - phase1_delay)

if __name__ == '__main__':
    main()

