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
    #output = Popen("ping 10.0.0.1 -c 10",stdout=PIPE,shell=True)
    #string = output.communicate()[0]
    #splitted = string.split('/')
    #timeout = 0.001 * float(splitted[4]) * 40
    timeout = 0.04
    print "Timeout is: " + str(timeout)
    print "waiting"
    while True:
        if datetime.datetime.now().strftime('%S') == '00':
            break
    print "running"
    recv_array = []
    cmd = "timeout " + str(timeout) + " ping 10.0.0.1 -c 1 || echo Failed"
    k = 0
    intervals=[]
    file = open("/home/sdn/covert_channel/h2_log.txt", "w")
    for i in range(message_length):
        start_time=time.time()
        print "Round" + str(k) + " is started at " + datetime.datetime.now().strftime('%H:%M:%S')
        file.write("Round" + str(k) + " is started at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        k = k + 1
        time.sleep(delta_s)
        phase2_start = time.time()
        file.write("---" + "(P2)Tried to check received bit at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        output = Popen(cmd,stdout=PIPE,shell=True)
        response = output.communicate()[0]
        if response == 'Failed\n':
            recv_array.append('1')
            file.write("---" + "The received bit detected and it is \"1\": " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        else:
            recv_array.append('0')
            file.write("---" + "The received bit detected and it is \"0\": " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        phase2_finish = time.time()
        phase2_delay = phase2_finish - phase2_start
        print phase2_delay
        time.sleep(delta_r - phase2_delay + delta_p)
        stop_time = time.time()
        time_difference = stop_time - start_time
        intervals.append(time_difference)
        file.write("---" + "Round" + str(k) + "is finished at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        file.write("---" + "Round" + str(k) + "taken time: " + str(time_difference) + "\n")
    avg_round_time = sum(intervals) / len(intervals)
    file.write("---------------------------------\n")
    file.write("Average round duration is: " + str(avg_round_time)+ "\n")
    file.close()
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
                                                                                                                              
