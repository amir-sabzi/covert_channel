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
    for element in binary_array:
        start_time=time.time()
        print "Round" + str(k) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S')
        file.write("Round" + str(k) + " is started at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        k = k + 1
        if element == '1':
            file.write("---" + "Tried to send bit \"1\" at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
            ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff" , src="00:00:00:00:00:01")/ARP(pdst="10.0.0.3"),timeout=0.05)
        else:
            file.write("---" + "Tried to send bit \"0\" at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        file.write("---" + "Sending bit considered DONE! at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        time.sleep(delta_s + delta_r + delta_p)
        stop_time = time.time()
        time_difference = stop_time - start_time
        file.write("---" + "Round" + str(k) + "taken time: " + str(time_difference) + "\n")


if __name__ == '__main__':
    main()

