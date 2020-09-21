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
    print "Calculatiing Timeout"
    output = Popen("ping 10.0.0.1 -c 10",stdout=PIPE,shell=True)
    string = output.communicate()[0]
    splitted = string.split('/')
    timeout = 0.001 * float(splitted[4]) * 40
    timeout = 0.03
    print "Timeout is: " + str(timeout)
    print "waiting"
    while True:
        if datetime.datetime.now().strftime('%S') == '00':
            break
    print "running"
    recv_array = []
    cmd = "timeout " + str(timeout) + " ping 10.0.0.1 -c 1 || echo Failed"
    k = 0
    for i in range(message_length):
	start_time=time.time()
        print "Round" + str(k) + " is started at " + datetime.datetime.now().strftime('%H:%M:%S')
        k = k + 1
        time.sleep(delta_s)
        output = Popen(cmd,stdout=PIPE,shell=True)
        response = output.communicate()[0]
        if response == 'Failed\n':
            recv_array.append('1')
            print "1"
        else:
            recv_array.append('0')
            print("0")
        time.sleep(delta_r + delta_p)
	stop_time = time.time()
	time_difference = stop_time - start_time
	print "elapsed time" + str(time_difference) 
    print "Received Bitstring"
    print recv_array
    print "Sended Bitstring"
    print binary_array
    counter = 0
    for i in range(message_length):
        if recv_array[i] != binary_array[i]:
            counter = counter + 1
    error_ratio = float(counter)/float(message_length)
    print "Error ratio is: " + str(error_ratio)

if __name__ == '__main__':
    main()
                                                                                                                              
