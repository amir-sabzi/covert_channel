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
    cmd = "timeout 0.08 ping 10.0.0.2 -c 1"
    cmd_omitted = "timeout 0.0005 ping 10.0.0.2 -c 1"
    intervals = []
    recv_array = []
    log = open("/home/amirs97/covert_channel/Two_malicious_hosts/calibration/receiver_calibration_log.txt", "w")
    cal_log = open("/home/amirs97/covert_channel/Two_malicious_hosts/calibration/calibration_log.txt", "w")
    i = 0
    k = 0
    temp = ""
    recv_message = ""
    while True:
        print "Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f')
        log.write("Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        time.sleep(calibration_delta_1)
        phase2_start = time.time()
        output_ommited = Popen(cmd_omitted,stdout=PIPE,shell=True)
        output = Popen(cmd,stdout=PIPE,shell=True)
        string = output.communicate()[0]
        splitted = string.split('/')
        if len(splitted)> 4:
            cal_log.write("sent_bit:" + callibration_array[i] +  ", delay:"+ splitted[4] +"\n")
            if float(splitted[4])  > 9 :
                recv_array.append('1')
                temp = temp + "1"
            else:
                recv_array.append('0')
                temp = temp + "0"
        else:
            print "nan"
            recv_array.append('NAN')
        phase2_finish = time.time()
        phase2_delay = phase2_finish - phase2_start
        print phase2_delay
        time.sleep(calibration_delta_2 - phase2_delay)
        i = i + 1
        if(i >= callibration_array_size):
            break
    
    print "Received Bitstring"
    print recv_array
    print "Sent Bitstring"
    print callibration_array
    counter = 0
    for i in range(callibration_array_size):
        if recv_array[i] != callibration_array[i]:
            counter = counter + 1
            print "At round: " + str(i) + " sended: " + callibration_array[i] + ", but received: " + recv_array[i] + "\n"
    error_ratio = float(counter)/float(callibration_array_size)
    print "Error ratio is: " + str(error_ratio)
    log.close()
    cal_log.close()
if __name__ == '__main__':
    main()


