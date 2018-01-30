'''
Created on Jan 19, 2018

@author: ehagan
'''
# more tuple unpacking
print(divmod(20, 8))
t = (30, 8)
print(divmod(*t))
# unpacking by prefixing an arg with *
for x in [(2, 4), (1, 2, 5), (3, 6, 1, 4)]:
    print('Adding {1} items to get {0}'.format(sum(x), len(x)))

*head, a, b = range(6)
print(head)

a, d, *head, e, f = range(6)
print(head)
