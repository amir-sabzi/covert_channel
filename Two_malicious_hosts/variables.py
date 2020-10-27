import random
import string 
delta_1 = 0.08
delta_2 = 0.045
byte_num = 128
message_length = (byte_num + 1) * 8
sent_message = "7bU4ETM9cciphU280pVqr5UFpeRE8BZpEemmSWzEBMzi3Bxt4P9rtQfIdPhlHCNI1CbHV2bey75NK6sZ8MXDgbI7DR6zQF6vHulUPYp2T98Nn7ur99EALdALozDEMKQP"
b = [ord(i) for i in sent_message] 
c = ['1' + '{0:07b}'.format(i) for i in b]
c.append('10000000')
d = [list(i) for i in c]
send_array = [item for sublist in d for item in sublist]
#send_array = ['1', '0', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '1', '1', '0', '1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '1']
#send_array = ['0', '1', '0', '1', '0']
