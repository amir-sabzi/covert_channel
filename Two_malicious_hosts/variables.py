import random
import string 
delta_1 = 0.07
delta_2 = 0.03
byte_num = 128
message_length = (byte_num + 1) * 8
a = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(byte_num))
b = [ord(i) for i in a] 
c = ['1' + '{0:07b}'.format(i) for i in b]
c.append('00000000')
d = [list(i) for i in c]
send_array = [item for sublist in d for item in sublist]
#send_array = ['1', '0', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '1', '1', '0', '1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '1']
#send_array = ['0', '1', '0', '1', '0']
