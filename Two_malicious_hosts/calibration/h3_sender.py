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
    log = open("/home/amirs97/covert_channel/Two_malicious_hosts/calibration/sender_calibration_log.txt", "w")
    i = 1
    for element in callibration_array:
        calibration_phase1_start = time.time()
        log.write("Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        if element == '1':
            srp(Ether(dst="ff:ff:ff:ff:ff:ff" , src="00:00:00:00:00:01")/ARP(pdst="10.0.0.2"),timeout=0.05)
        calibration_phase1_finish = time.time()
        calibration_phase1_delay = calibration_phase1_finish - calibration_phase1_start
        time.sleep(calibration_delta_1 - calibration_phase1_delay)
        time.sleep(calibration_delta_2)
        i += 1
    log.close()
if __name__ == '__main__':
    main()

