import sys
import socket
from scipy import special as sp
import numpy as np
import random
import struct
import time
from subprocess import Popen, PIPE
from scapy.all import *
import shlex
import datetime
from variables import *

def qfunc(x):
    return 0.5-0.5*sp.erf(x/np.sqrt(2))


def Treshold_cal(one_delays,zero_delays):
    one_mean = np.mean(one_delays)
    one_var = np.var(one_delays)
    zero_mean = np.mean(zero_delays)
    zero_var = np.var(zero_delays)
    T = np.linspace(0,50,10001)
    P_err = 0.5 * (qfunc((T-zero_mean)/np.sqrt(zero_var)) + qfunc(-(T-one_mean)/np.sqrt(one_var)))
    index_min = np.argmin(P_err)
    return T[index_min]



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
    ones_delay = []
    zeros_delay = []
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
            if callibration_array[i] ==  '0' :
                zeros_delay.append(float(splitted[4]))
            else:
                ones_delay.append(float(splitted[4]))
        else:
            print "nan"
        phase2_finish = time.time()
        phase2_delay = phase2_finish - phase2_start
        print phase2_delay
        time.sleep(calibration_delta_2 - phase2_delay)
        i = i + 1
        if(i >= callibration_array_size):
            break
    T = Treshold_cal(ones_delay,zeros_delay)
    print "The Calculated Treshold is: " + str(T)
    err_count = sum(i > T for i in zeros_delay) + sum(i < T for i in ones_delay)
    error_ratio = float(err_count)/float(callibration_array_size)
    print "Error ratio is: " + str(error_ratio)
    log.close()
    cal_log.close()
if __name__ == '__main__':
    main()


