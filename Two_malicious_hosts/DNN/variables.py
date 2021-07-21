import random
import string
import numpy as np 

def transfer_to_desired_format(message):
    b = [ord(i) for i in message] 
    c = ['1' + '{0:07b}'.format(i) for i in b]
    c.append('10000000')
    d = [list(i) for i in c]
    array = [item for sublist in d for item in sublist]
    return array


syncTrial_duration = 1
number_of_tests = 1
delta_1 = 0.12
delta_2 = 0.05
train_set_byte_num = 64
byte_num = 128
transmission_message = "x28zQGrukeC3v5nYAIEeXD6p3afEeMYZy6w8P4ZgfpuOtvwsEYyqu8sg8D8MNsHC"
training_message = "7bU4ETM9cciphU280pVqr5UFpeRE8BZpEemmSWzEBMzi3Bxt4P9rtQfIdPhlHCNI1CbHV2bey75NK6sZ8MXDgbI7DR6zQF6vHulUPYp2T98Nn7ur99EALdALozDEMKQP"

callibration_array = transfer_to_desired_format(training_message)
transmission_array = transfer_to_desired_format(transmission_message)

message_length = len(transmission_array)
callibration_array_size = len(callibration_array)
