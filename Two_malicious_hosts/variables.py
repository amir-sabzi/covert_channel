import random
import string 
delta_1 = 0.08
delta_2 = 0.04
byte_num = 50
message_length = (byte_num + 1) * 8
a = "Neyd1gFw1pitrZq30ud040qLr2SvfTPTXQO6Z4y9qct4TUQ6Rn"
b = [ord(i) for i in a] 
c = ['1' + '{0:07b}'.format(i) for i in b]
c.append('00000000')
d = [list(i) for i in c]
send_array = [item for sublist in d for item in sublist]
#send_array = ['1', '0', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '1', '1', '0', '1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '1']
#send_array = ['0', '1', '0', '1', '0']
