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
    cmd = "timeout 0.03 ping 10.0.0.2 -c 1"
    cmd_omitted = "timeout 0.0005 ping 10.0.0.2 -c 1"
    k = 0
    intervals = []
    recv_array = []
    log = open("/home/amirs97/covert_channel/Two_malicious_hosts/receiver_log.txt", "w")
    i = 0
    k = 0
    temp = ""
    recv_message = ""
    while True:
        print "Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f')
        log.write("Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
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
                temp = temp + "1"
            else:
                recv_array.append('0')
                temp = temp + "0"
        else:
            print "nan"
            recv_array.append('NAN')
        k = k + 1
        if k == 8:
            if(temp == "10000000"):
                print "End of Massage Recieved"
                break
            else:
                recv_message = recv_message + char(int(temp[1:],2))
                temp = ""
                k = 0
        phase2_finish = time.time()
        phase2_delay = phase2_finish - phase2_start
        print phase2_delay
        time.sleep(delta_2 - phase2_delay)
        i = i + 1
    
    print "Received Bitstring"
    print recv_message
    print "Sent Bitstring"
    print sent_message
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


