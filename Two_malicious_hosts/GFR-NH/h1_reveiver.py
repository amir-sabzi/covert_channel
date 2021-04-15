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
def calibration(receiving_array,receiving_array_size,interface_name):
    print "waiting for synchronization..."
    # A synchronization part, should be replaced by a NTP server request.
    while True:                             
        if datetime.datetime.now().strftime('%S') == '00':
            break
    print "calibration phase running..."

    # As I described in the report, after vm-migration, the first try to ping other severs will fail. 
    # Thus, with the cmd_omitted we just send first ping request and we will not wait for the response.
    cmd = "timeout 0.08 ping -I " + interface_name + " 10.0.0.2 -c 1"  
    cmd_omitted = "timeout 0.0005 ping -I " + interface_name + " 10.0.0.2 -c 1"

    # I defined two log-file. First, the "receiver_calibration_log.txt", and I use this to record timing of rounds and packet arrival times.
    # The second log file is "calibration_log.txt". This file is used for experimental purpose.
    # Caution: if you are running this code on your machine, you should consider changing the directroy of each log file.
    log = open("/home/amirs97/covert_channel/Two_malicious_hosts/GFR-NH/logs/receiver_calibration_log_" + interface_name + ".txt", "w")
    cal_log = open("/home/amirs97/covert_channel/Two_malicious_hosts/GFR-NH/logs/calibration_log_" + interface_name + ".txt", "w")
    cal_log.write("bit, RTT" + "\n")
    ones_delay = []
    zeros_delay = []

    # In this for loop, the receiver will receive the data based on the algorithm that I described. But here we just want to calibrate the receiver, Thus...
    # ... we just will record the ping packet RTT to determine the treshold based on that.
    for i in range(receiving_array_size):
        #print "Calibration Phase, Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f')
        log.write("Round" + str(i) +  " is started at " + datetime.datetime.now().strftime('%H:%M:%S:%f') + "\n")
        time.sleep(calibration_delta_1)
        phase2_start = time.time()
        output_ommited = Popen(cmd_omitted,stdout=PIPE,shell=True)
        output = Popen(cmd,stdout=PIPE,shell=True)
        # All subsequent actions are just for extracting the RTT form the linux command line.
        string = output.communicate()[0]
        splitted = string.split('/')
        if len(splitted)> 4:
            cal_log.write(receiving_array[i] +  ","+ splitted[4] +"\n")
            if receiving_array[i] ==  '0' :
                zeros_delay.append(float(splitted[4]))
            else:
                ones_delay.append(float(splitted[4]))
        else:
            print "nan"
        phase2_finish = time.time()
        phase2_delay = phase2_finish - phase2_start
        print phase2_delay
        # In this line, I tried to compensate the time spent to run the code. It helps us to stay synchronized with the sender.
        # Causion: if we have the phase2_delay > calibration_delta_2, we will got the error an running code will be terminated, and it reasonable because that means...
        # ...we have chosen insufficient values for delta 1 and delta 2.
        time.sleep(calibration_delta_2 - phase2_delay)

    # Calculating the treshold using the data extracted in previous loop.
    T = Treshold_cal(ones_delay,zeros_delay)

    # Here we calculate expected error. As I said before, we choose a treshold that can minimize the error function. We defined this error function based on assumption that...
    # ...the samples come from a Gaussian distribution. The error will minimize but it may not be zoro. Thus, I reported the exptected value for the erorr. I will compare it...
    # ...with the final error value at the end.
    err_count = sum(i > T for i in zeros_delay) + sum(i < T for i in ones_delay)
    error_ratio = float(err_count)/float(receiving_array_size)
    print "the calculated threshold for " + interface_name + " is: "+ str(T) + "\n"
    print "the expected error for " + interface_name + " is: "+ str(error_ratio) + "\n"
    cal_log.write("the calculated threshold is: "+ str(T) + "\n")
    cal_log.write("the expected error is: "+ str(error_ratio) + "\n")

    log.close()
    cal_log.close()





def main():

    # creating thread
    t0 = threading.Thread(target=calibration, args=(t0_array,callibration_array_size/interface_num,"h1-eth0",))
    t1 = threading.Thread(target=calibration, args=(t1_array,callibration_array_size/interface_num,"h1-eth1",))
    t2 = threading.Thread(target=calibration, args=(t2_array,callibration_array_size/interface_num,"h1-eth2",))

    # starting thread 0
    t0.start()
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 0 is completely executed
    t0.join()
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
  
    # both threads completely executed
    print("Done!")
if __name__ == '__main__':
    main()


