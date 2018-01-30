'''
Created on Jan 19, 2018
@author: ehagan
'''
# slicing works on all sequence typles
s = 'bicycle'
# slicing with a stride s[a:b:c]
# ie sequence[start:stop:step]
# start=a end = c-1 at step=c
print(s[::3])  # start=s[0] end=s[len(s)-1] step=3
# slicing in reverse take negative stride
print(s[::-1])
print(s[::-2])
print(s[::-3])
