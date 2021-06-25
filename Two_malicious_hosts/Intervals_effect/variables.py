import random
import string
import numpy as np 


delta_1_array = np.flip(np.linspace(0.06,1,8), axis=None)
delta_2_array =  np.flip(np.linspace(0.04,0.045,2), axis=None)


#delta_1 = 0.09
#delta_2 = 0.06

syncTrial_duration = 1
number_of_tests = 32
calibration_delta_1 = 0.3
calibration_delta_2 = 0.3
byte_num = 4
callibration_array_size = 128
callibration_array = ['1','0'] * int(callibration_array_size/2)
message_length = (byte_num + 1) * 8
#sent_message = "7bU4ETM9cciphU280pVqr5UFpeRE8BZpEemmSWzEBMzi3Bxt4P9rtQfIdPhlHCNI1CbHV2bey75NK6sZ8MXDgbI7DR6zQF6vHulUPYp2T98Nn7ur99EALdALozDEMKQP"
sent_message = "7bU4"
b = [ord(i) for i in sent_message] 
c = ['1' + '{0:07b}'.format(i) for i in b]
c.append('10000000')
d = [list(i) for i in c]
send_array = [item for sublist in d for item in sublist]
print(delta_2_array)

