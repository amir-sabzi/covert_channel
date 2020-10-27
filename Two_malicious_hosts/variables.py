import random
import string 
delta_1 = 0.08
delta_2 = 0.045
byte_num = 128
message_length = (byte_num + 1) * 8
a = "gPet4gD4hDjuTKkAP25iKLDBjHefd2zk0qtksQcd9RAiDhe5ism7zj8jGNLN86i6z58oXaMnOzXn42NS7r8H0Pjf3KAF2s04bMJcjK9PH7QahULBbwD9c8fZCpwlwtwg"
b = [ord(i) for i in a] 
c = ['1' + '{0:07b}'.format(i) for i in b]
c.append('00000000')
d = [list(i) for i in c]
send_array = [item for sublist in d for item in sublist]
#send_array = ['1', '0', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '1', '1', '0', '1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '1']
#send_array = ['0', '1', '0', '1', '0']
