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


def sender(sending_thread_array,delta_1,delta_2):
    print "waiting for synchronization..."
    while True:
        if datetime.datetime.now().strftime('%S') == '00':
            break
    print "running"
    #cmd = "timeout 0.05 nping --source-mac 00:00:00:00:00:01 10.0.0.2 -c 1"
    i = 1
    for element in sending_thread_array:
        calibration_phase1_start = time.time()
        print "Calibration Phase, Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f')
        if element == '1':
            srp(Ether(dst="ff:ff:ff:ff:ff:ff" , src="00:00:00:00:00:01")/ARP(pdst="10.0.0.2"),timeout=(delta_1/8),verbose=0)
        calibration_phase1_finish = time.time()
        calibration_phase1_delay = calibration_phase1_finish - calibration_phase1_start
        print(calibration_phase1_delay)
        time.sleep(delta_1 - calibration_phase1_delay)
        time.sleep(delta_2)
        i += 1
    time.sleep(syncTrial_duration)

def main():

    for delta_1 in delta_1_array:
        for delta_2 in delta_2_array:
            sender(callibration_array,delta_1,delta_2)
    print("Done!")

if __name__ == '__main__':
    main()
