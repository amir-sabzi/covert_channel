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
    cmd_omitted = "timeout 0.01 ping 10.0.0.2 -c 1"
    k = 0
    intervals = []
    recv_array = []
    log = open("/home/amirs97/covert_channel/Two_malicious_hosts/receiver_log.txt", "w")
    for i in range(message_length):
        print "Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f')
        log.write("Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f'))
        time.sleep(delta_1)
        phase2_start = time.time()
        output_ommited = Popen(cmd_omitted,stdout=PIPE,shell=True)
        output = Popen(cmd,stdout=PIPE,shell=True)
        string = output.communicate()[0]
        splitted = string.split('/')
        if len(splitted)> 4:
            print
            if float(splitted[4])  > 7 :
                recv_array.append('1')
            else:
                recv_array.append('0')
        else:
            print "nan"
            recv_array.append('NAN')
        phase2_finish = time.time()
        phase2_delay = phase2_finish - phase2_start
        print phase2_delay
        time.sleep(delta_2 - phase2_delay)
    print "Received Bitstring"
    print recv_array
    print "Sended Bitstring"
    print send_array
    counter = 0
    for i in range(message_length):
        if recv_array[i] != send_array[i]:
            counter = counter + 1
            print "At round: " + str(i) + " sended: " + send_array[i] + ", but received: " + recv_array[i] + "\n"
    error_ratio = float(counter)/float(message_length)
    print "Error ratio is: " + str(error_ratio)
    log.close()

if __name__ == '__main__':
    main()


