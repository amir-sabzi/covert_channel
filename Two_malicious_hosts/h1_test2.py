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
    cmd = "timeout 0.05 ping 10.0.0.2 -c 1"
    cmd_omitted = "timeout 0.05 ping 10.0.0.2 -c 1"
    k = 0
    intervals = []
    new = open("/home/amirs97/covert_channel/Two_malicious_hosts/secondPing_delay.txt", "w")
    old = open("/home/amirs97/covert_channel/Two_malicious_hosts/thirdPing_delay.txt", "w")
    for i in range(sample_num):
        print "Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S')
        time.sleep(delta_1)
        phase2_start = time.time()
        output_ommited = Popen(cmd_omitted,stdout=PIPE,shell=True)
        output = Popen(cmd,stdout=PIPE,shell=True)
        string = output.communicate()[0]
        splitted = string.split('/')
        if len(splitted)> 4:
            new.write(splitted[4] + "\n")
        else:
            new.write("NAN" + "\n")
        phase2_finish = time.time()
        phase2_delay = phase2_finish - phase2_start
        print phase2_delay
        time.sleep(delta_2 - phase2_delay)

        phase3_start = time.time()
        output_ommited = Popen(cmd_omitted,stdout=PIPE,shell=True)
        output = Popen(cmd,stdout=PIPE,shell=True)
        string = output.communicate()[0]
        splitted = string.split('/')
        if len(splitted)> 4:
            old.write(splitted[4] + "\n")
        else:
            old.write("NAN" + "\n")
        phase3_finish = time.time()
        phase3_delay = phase3_finish - phase3_start
        print phase3_delay
        time.sleep(delta_3 - phase3_delay)

    new.close()
    old.close()
if __name__ == '__main__':
    main()


