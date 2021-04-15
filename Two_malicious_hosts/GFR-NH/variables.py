import random
import string 
delta_1 = 0.09
delta_2 = 0.06
interface_num = 3
number_of_tests = 32
calibration_delta_1 = 0.3
calibration_delta_2 = 0.3
byte_num = 4
callibration_array_size = 1200 #shoud be devidable by 6
callibration_array = ['0','0','0','1','1','1'] * int(callibration_array_size/6)
t0_array = []
t1_array = []
t2_array = []
for i in range(callibration_array_size/interface_num):
    t0_array.append(callibration_array[interface_num*i])
    t1_array.append(callibration_array[interface_num*i + 1])
    t2_array.append(callibration_array[interface_num*i + 2])


message_length = (byte_num + 1) * 8
#sent_message = "7bU4ETM9cciphU280pVqr5UFpeRE8BZpEemmSWzEBMzi3Bxt4P9rtQfIdPhlHCNI1CbHV2bey75NK6sZ8MXDgbI7DR6zQF6vHulUPYp2T98Nn7ur99EALdALozDEMKQP"
sent_message = "7bU4"
b = [ord(i) for i in sent_message] 
c = ['1' + '{0:07b}'.format(i) for i in b]
c.append('10000000')
d = [list(i) for i in c]
send_array = [item for sublist in d for item in sublist]



