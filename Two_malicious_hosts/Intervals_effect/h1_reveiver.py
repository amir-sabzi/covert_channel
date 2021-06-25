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

# In this function, I implemented the statistical method that I have reported in the document to calculate a proper treshold.
def Treshold_cal(one_delays,zero_delays):  
    one_mean = np.mean(one_delays)
    one_var = np.var(one_delays)
    zero_mean = np.mean(zero_delays)
    zero_var = np.var(zero_delays)
    T = np.linspace(0,50,10001)
    P_err = 0.5 * (qfunc((T-zero_mean)/np.sqrt(zero_var)) + qfunc(-(T-one_mean)/np.sqrt(one_var))) 
    index_min = np.argmin(P_err)
    return T[index_min]

# This function is designed to perform calibration and find a proper treshold to determine reveived bit is one or zero. 
# The input is the calibration array which in general case is a square wave. The output is the treshold(T) and and expected_error(E) using this treshold.
def calibration(callibration_array,callibration_array_size,delta_1,delta_2):
    print "waiting for synchronization..."
    # A synchronization part, should be replaced by a NTP server request.
    while True:                             
        if datetime.datetime.now().strftime('%S') == '00':
            break
    print "calibration phase running..."

    # As I described in the report, after vm-migration, the first try to ping other severs will fail. 
    # Thus, with the cmd_omitted we just send first ping request and we will not wait for the response.
    cmd_timeout = delta_2/2
    cmd = "timeout " + str(cmd_timeout) + " ping 10.0.0.2 -c 1"
    cmd_omitted = "timeout 0.0005 ping 10.0.0.2 -c 1"

    # I defined two log-file. First, the "receiver_calibration_log.txt", and I use this to record timing of rounds and packet arrival times.
    # The second log file is "calibration_log.txt". This file is used for experimental purpose.
    # Caution: if you are running this code on your machine, you should consider changing the directroy of each log file.
    ones_delay = []
    zeros_delay = []
    nan_counter = 0
    # In this for loop, the receiver will receive the data based on the algorithm that I described. But here we just want to calibrate the receiver, Thus...
    # ... we just will record the ping packet RTT to determine the treshold based on that.
    for i in range(callibration_array_size):
        print "Calibration Phase, Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f')
        time.sleep(delta_1)
        phase2_start = time.time()
        output_ommited = Popen(cmd_omitted,stdout=PIPE,shell=True)
        output = Popen(cmd,stdout=PIPE,shell=True)
        # All subsequent actions are just for extracting the RTT form the linux command line.
        string = output.communicate()[0]
        splitted = string.split('/')
        if len(splitted)> 4:
            if callibration_array[i] ==  '0' :
                zeros_delay.append(float(splitted[4]))
            else:
                ones_delay.append(float(splitted[4]))
        else:
            print "nan"
            nan_counter += 1
        phase2_finish = time.time()
        phase2_delay = phase2_finish - phase2_start
        # In this line, I tried to compensate the time spent to run the code. It helps us to stay synchronized with the sender.
        # Causion: if we have the phase2_delay > calibration_delta_2, we will got the error an running code will be terminated, and it reasonable because that means...
        # ...we have chosen insufficient values for delta 1 and delta 2.
        time.sleep(delta_2 - phase2_delay)
    

    # I add this part to reconfigure flows for the next trial
    syncInterval_start = time.time()
    nextTtrial_cmd = "timeout 0.5 ping 10.0.0.2 -c 1"
    output = Popen(cmd,stdout=PIPE,shell=True)
    syncInterval_stop = time.time()
    syncInterval_delay = syncInterval_start - syncInterval_stop
    time.sleep(syncTrial_duration - syncInterval_delay)


    # Calculating the treshold using the data extracted in previous loop.
    T = Treshold_cal(ones_delay,zeros_delay)

    # Here we calculate expected error. As I said before, we choose a treshold that can minimize the error function. We defined this error function based on assumption that...
    # ...the samples come from a Gaussian distribution. The error will minimize but it may not be zoro. Thus, I reported the exptected value for the erorr. I will compare it...
    # ...with the final error value at the end.
    print("The number of nan bits are: " + str(nan_counter)
    err_count = sum(i > T for i in zeros_delay) + sum(i < T for i in ones_delay) + nan_counter
    error_ratio = float(err_count)/float(callibration_array_size)
    return T, error_ratio





def main():
    TE_log = open("/home/amirs97/covert_channel/Two_malicious_hosts/Intervals_effect/Intervals_log_exp1.txt", "w")
    TE_log.write("delta_1,delta_2,Treshold,Error" + "\n")
    for delta_1 in delta_1_array:
        for delta_2 in delta_2_array:
            threshold, expected_error = calibration(callibration_array,callibration_array_size,delta_1,delta_2)
            print "The Calculated Treshold is: " + str(threshold)
            print "Error ratio using this treshold is: " + str(expected_error)
            TE_log.write(str(delta_1)+","+str(delta_2)+","+str(threshold)+","+str(expected_error) + "\n")

    TE_log.close()
if __name__ == '__main__':
    main()


