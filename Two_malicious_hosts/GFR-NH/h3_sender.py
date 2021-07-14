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
    cmd_timeout = calibration_delta_1 * 3/5
    cmd = "timeout " + str(cmd_timeout) + " nping " + " -e " + interface_name + " --source-mac " + source_mac + " 10.0.0.2 -c 1"
    log = open("/home/amirs97/covert_channel/Two_malicious_hosts/calibration/sender_calibration_log_" + interface_name + ".txt", "w")
    i = 1
    for element in sending_thread_array:
        calibration_phase1_start = time.time()
        if element == '1':
            #srp(Ether(dst="ff:ff:ff:ff:ff:ff" , src=source_mac)/ARP(pdst="10.0.0.2"),timeout=0.05,iface=interface_name,verbose=0)
            output = Popen(cmd,stdout=PIPE,shell=True)
        calibration_phase1_finish = time.time()
        calibration_phase1_delay = calibration_phase1_finish - calibration_phase1_start
        print(calibration_delta_1 - calibration_phase1_delay)
        time.sleep(calibration_delta_1 - calibration_phase1_delay)
        time.sleep(calibration_delta_2)
        i += 1
    log.close()

def main():
    # creating thread
    thread_list = []
    for i in range(interface_num):
        callibration_array_temp = [row[i] for row in calibration_matrix]
        if (i < 10):
            src_macAddr = '00:00:00:00:01:0' + str(i)
        else:
            src_macAddr = '00:00:00:00:01:' + str(i)
        interface_name = "h3-eth" + str(i)
        thread = threading.Thread(target=sender, args=(callibration_array_temp,src_macAddr,interface_name,)) 
        thread_list.append(thread)

    # starting threads
    for thread in thread_list:
        thread.start()

    # wait until threads are completely executed
    for thread in thread_list:
        thread.join()

    # threads completely executed
    print("Done!")
if __name__ == '__main__':
    main()

