import random
import string 
delta_1 = 0.09
delta_2 = 0.06
calibration_delta_1 = 0.15
calibration_delta_2 = 0.1
byte_num = 4
callibration_array_size = 24
callibration_array = ['1','0'] * int(callibration_array_size/2)
message_length = (byte_num + 1) * 8
#sent_message = "7bU4ETM9cciphU280pVqr5UFpeRE8BZpEemmSWzEBMzi3Bxt4P9rtQfIdPhlHCNI1CbHV2bey75NK6sZ8MXDgbI7DR6zQF6vHulUPYp2T98Nn7ur99EALdALozDEMKQP"
sent_message = "7bU4"
b = [ord(i) for i in sent_message] 
c = ['1' + '{0:07b}'.format(i) for i in b]
c.append('10000000')
d = [list(i) for i in c]
send_array = [item for sublist in d for item in sublist]



