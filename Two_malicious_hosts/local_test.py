import random
import string
length = 128
a = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
print a 
b = [ord(i) for i in a] 
#print b
c = ['1' + '{0:07b}'.format(i) for i in b]
c.append('00000000')
#print c
d = [list(i) for i in c]
#print d
flat_list = [item for sublist in d for item in sublist]
#print flat_list
