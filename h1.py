import sys
import socket
import random
import struct
import time
import datetime
from subprocess import Popen, PIPE
from scapy.all import *
import shlex
from variables import *


def main():
    print "waiting"
    file = open("/home/sdn/covert_channel/h1_log.txt", "w")
    while True:
        if datetime.datetime.now().strftime('%S') == '00':
            break
    print "running"
    timeout = 0.1
    cmd = "timeout 0.1 ping 10.0.0.2 -c 1"
    k = 0
    intervals = []
    for i in range(message_length):
        start_time=time.time()
        print "Round-" + str(k) + " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f')
        file.write("Round-" + str(k) + " is started at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        k = k + 1
        time.sleep(delta_s + delta_r)
        phase3_start = time.time()
        file.write("---" + "(P3)tried to redefine flows on the switch at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        output = Popen(cmd,stdout=PIPE,shell=True)
        response = output.communicate()[0]
        file.write("---" + "(P3)flow reconfiguration considered DONE! at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        phase3_finish = time.time()
        phase3_delay = phase3_finish - phase3_start
        file.write("---" + "(P3)Phase-3 delay is: " + str(phase3_delay) + "\n")
        time.sleep(delta_p - phase3_delay)
        stop_time=time.time()
        time_difference = stop_time - start_time
        intervals.append(time_difference)
        file.write("---" + "Round-" + str(k) + " is finished at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        file.write("---" + "Round-" + str(k) + " taken time: " + str(time_difference) + "\n")
    avg_round_time = sum(intervals) / len(intervals)
    file.write("---------------------------------\n")
    file.write("Average round duration is: " + str(avg_round_time) +  "\n")
    file.close()
if __name__ == '__main__':
    main()


