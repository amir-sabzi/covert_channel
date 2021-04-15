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
import threading

def sender(sending_thread_array,source_mac,interface_name):
    print "waiting for synchronization..."
    while True:
        if datetime.datetime.now().strftime('%S') == '00':
            break
    print "running"
    #cmd = "timeout 0.05 nping --source-mac 00:00:00:00:00:01 10.0.0.2 -c 1"
    log = open("/home/amirs97/covert_channel/Two_malicious_hosts/calibration/sender_calibration_log_" + interface_name + ".txt", "w")
    i = 1
    for element in sending_thread_array:
        calibration_phase1_start = time.time()
        log.write("Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        if element == '1':
            srp(Ether(dst="ff:ff:ff:ff:ff:ff" , src=source_mac)/ARP(pdst="10.0.0.2"),timeout=0.05,iface=interface_name)
        calibration_phase1_finish = time.time()
        calibration_phase1_delay = calibration_phase1_finish - calibration_phase1_start
        time.sleep(calibration_delta_1 - calibration_phase1_delay)
        time.sleep(calibration_delta_2)
        i += 1
    log.close()

def main():
    # creating thread
    t0 = threading.Thread(target=sender, args=(t0_array,"00:00:00:00:01:00","h3-eth0",))
    t1 = threading.Thread(target=sender, args=(t1_array,"00:00:00:00:01:01","h3-eth1",))
    t2 = threading.Thread(target=sender, args=(t2_array,"00:00:00:00:01:02","h3-eth2",))

    # starting thread 0
    t0.start()
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 0 is completely executed
    t0.join()
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
  
    # both threads completely executed
    print("Done!")

if __name__ == '__main__':
    main()

