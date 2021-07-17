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


def sender(sending_thread_array):
    print "waiting for synchronization..."
    while True:
        if datetime.datetime.now().strftime('%S') == '00':
            break
    print "running"
    cmd_timeout = delta_1 * 3/5
    cmd = "timeout " + str(cmd_timeout) + " nping --source-mac 00:00:00:00:00:01 10.0.0.2 -c 1"
    i = 1
    for element in sending_thread_array:
        calibration_phase1_start = time.time()
        print "Calibration Phase, Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f')
        if element == '1':
            #srp(Ether(dst="ff:ff:ff:ff:ff:ff" , src="00:00:00:00:00:01")/ARP(pdst="10.0.0.2"),timeout=(delta_1/20),verbose=0)
            output = Popen(cmd,stdout=PIPE,shell=True)
        calibration_phase1_finish = time.time()
        calibration_phase1_delay = calibration_phase1_finish - calibration_phase1_start
        print(calibration_phase1_delay)
        time.sleep(delta_1 - calibration_phase1_delay)
        time.sleep(delta_2)
        i += 1
    time.sleep(syncTrial_duration)

def sending():
    # Running as the calibration phase
    sender(callibration_array)

    # Running as the transmission phase
    sender(transmission_array)



def main():

    for i in range(number_of_tests):
        sending()

    print("Done!")

if __name__ == '__main__':
    main()
