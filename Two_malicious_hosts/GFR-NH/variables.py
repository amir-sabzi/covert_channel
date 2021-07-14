import random
import string 

interface_num = 10
number_of_tests = 32
calibration_delta_1 = 0.2
calibration_delta_2 = 0.12
byte_num = 4
callibration_array_size = 128
zeros = ['0'] * interface_num
ones = ['1'] * interface_num
calibration_matrix = [zeros,ones] * (callibration_array_size/2) # Each row corresponds to an interface. 


message_length = (byte_num + 1) * 8
#sent_message = "7bU4ETM9cciphU280pVqr5UFpeRE8BZpEemmSWzEBMzi3Bxt4P9rtQfIdPhlHCNI1CbHV2bey75NK6sZ8MXDgbI7DR6zQF6vHulUPYp2T98Nn7ur99EALdALozDEMKQP"
sent_message = "7bU4"
b = [ord(i) for i in sent_message] 
c = ['1' + '{0:07b}'.format(i) for i in b]
c.append('10000000')
d = [list(i) for i in c]
send_array = [item for sublist in d for item in sublist]
