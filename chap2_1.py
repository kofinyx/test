'''
Created on Jan 19, 2018

@author: ehagan
'''
# cartesian product using listcomp

sizes = ['S', 'M', 'L']
colors = ['red', 'green', 'orange']
tshirtlist = [(color, size) for color in colors for size in sizes]
print('{}\n{}'.format('This is a list', tshirtlist))
# tshirtlist is a list of tuples
# Using for loop to print only the
# colors and assign the sizes to a dummy '_'
for color, _ in tshirtlist:
    print(color)

# doing it with genexp
# if the sequence is not a list then a generator is the way to do it
tshirt = tuple((size, color) for color in colors for size in sizes)
print('{}\n{}'.format('This is a tuple', tshirt))

# genexp used and formated
print('{}'.format('This is each shirt'))
for shirt in ('{1} and {0}'.format(color, size) for color in colors for size in sizes):
    print(shirt)
# Slicing
print(tshirt[:1])
print(tshirtlist[len(tshirtlist) - 3:len(tshirtlist)])
