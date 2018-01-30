'''
Created on Jan 29, 2018

@author: ehagan
'''
from array import array
from random import random

myfloat = array('d', (random() for i in range(10**7)))
fp = open('myfloat.txt', 'wb')
myfloat.tofile(fp)
print(myfloat[-1])
fp.close()
myfloat2 = array('d')
fp = open('myfloat.txt', 'rb')
myfloat2.fromfile(fp, 10**7)
print(myfloat2[-1])
