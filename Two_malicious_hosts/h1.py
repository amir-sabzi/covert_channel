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
    cmd = "ping 10.0.0.2 -c 3"
    k = 0
    intervals = []
    new = open("/home/sdn/covert_channel/covert_channel/Two_malicious_hosts/new_flow_delay.txt", "w")
    old = open("/home/sdn/covert_channel/covert_channel/Two_malicious_hosts/existed_flow_delay.txt", "w")
    for i in range(sample_num):
        print "Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S')
        time.sleep(delta_1)
        phase2_start = time.time()
        output = Popen(cmd,stdout=PIPE,shell=True)
        string = output.communicate()[0]
        splitted = string.split('/')
        new.write(splitted[4] + "\n")
        phase2_finish = time.time()
        phase2_delay = phase2_finish - phase2_start
        time.sleep(delta_2 - phase2_delay)

        phase3_start = time.time()
        output = Popen(cmd,stdout=PIPE,shell=True)
        string = output.communicate()[0]
        splitted = string.split('/')
        old.write(splitted[4] + "\n")
        phase3_finish = time.time()
        phase3_delay = phase3_finish - phase3_start
        time.sleep(delta_3 - phase3_delay)

    new.close()
    old.close()
if __name__ == '__main__':
    main()


