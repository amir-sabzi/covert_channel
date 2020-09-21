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
    k = 0
    for element in binary_array:
	start_time=time.time()
        print "Round" + str(k) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S')
        k = k + 1
        if element == '1':
            ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff" , src="00:00:00:00:00:01")/ARP(pdst="10.0.0.3"),timeout=0.05)
        time.sleep(delta_s + delta_r + delta_p)
        stop_time = time.time()
        time_difference = stop_time - start_time
	print "elapsed time" + str(time_difference)


if __name__ == '__main__':
    main()

