import sys
import socket
import random
import struct
import time
from datetime import datetime, timezone
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
    timeout = 0.03
    cmd = "timeout 0.1 ping 10.0.0.2 -c 1"
    k = 0
    for i in range(message_length):
        start=time.time()
        print "Round" + str(k) + " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f')
        file.write("Round" + str(k) + " is started at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        k = k + 1
        time.sleep(delta_s + delta_r)
        file.write("---" + "tried to redefine flows on the switch at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        output = Popen(cmd,stdout=PIPE,shell=True)
        response = output.communicate()[0]
        file.write("---" + "flow reconfiguration considered DONE! at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        time.sleep(delta_p)
        file.write("---" + "Round" + str(k) + "is finished at: " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        time.sleep(delta_p)
        stop=time.time()
        file.write("---" + "Round" + str(k) + "taken time: " + str(stop-start) + "\n")
    file.close()
if __name__ == '__main__':
    main()


