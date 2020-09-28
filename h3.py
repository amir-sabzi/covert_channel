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
    k = 0
    file = open("/home/sdn/covert_channel/h3_log.txt", "w")
    intervals=[]
    for element in binary_array:
        start_time=time.time()
        print "Round" + str(k) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S')
        file.write("Round" + str(k) + " is started at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        k = k + 1
        phase1_start = time.time()
        if element == '1':
            file.write("---" + "Tried to send bit \"1\" at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
            ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff" , src="00:00:00:00:00:01")/ARP(pdst="10.0.0.3"),timeout=0.05)
        else:
            file.write("---" + "Tried to send bit \"0\" at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        phase1_finish = time.time()
        phase1_delay = phase1_finish - phase1_start
        file.write("---" + "Sending bit considered DONE! at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        time.sleep(delta_s + delta_r + delta_p - phase1_delay)
        stop_time = time.time()
        time_difference = stop_time - start_time
        intervals.append(time_difference)
        file.write("---" + "Round" + str(k) + "is finished at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        file.write("---" + "Round" + str(k) + "taken time: " + str(time_difference) + "\n")
    avg_round_time = sum(intervals) / len(intervals)
    file.write("---------------------------------\n")
    file.write("Average round duration is: " + str(avg_round_time)+ "\n")
    file.close()

if __name__ == '__main__':
    main()

