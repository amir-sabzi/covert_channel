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
    cmd = "timeout 0.05 nping --source-mac 00:00:00:00:00:01 10.0.0.2 -c 1"
    intervals=[]
    i = 0
    log = open("/home/amirs97/covert_channel/Two_malicious_hosts/sender_log.txt", "w")
    for element in send_array:
        print "Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f')
        log.write("Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        phase1_start=time.time()
        #print "Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S')
        #output = Popen(cmd,stdout=PIPE,shell=True)
        if element == '1':
            #output = Popen(cmd,stdout=PIPE,shell=True)
            srp(Ether(dst="ff:ff:ff:ff:ff:ff" , src="00:00:00:00:00:01")/ARP(pdst="10.0.0.2"),timeout=0.01)
        phase1_finish=time.time()
        phase1_delay = phase1_finish - phase1_start
        print phase1_delay
        time.sleep(delta_1 - phase1_delay)
        time.sleep(delta_2)
        i = i + 1
    log.close()
if __name__ == '__main__':
    main()

