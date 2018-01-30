'''
Created on Jan 19, 2018

@author: ehagan

'''
# Best way to build a sequence is by using listcomp
# or by using genexp

# build a list of unicode codepoints from a string
print("Using for loop")
symbols = "Ac$€£©¥Ω"
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# creating a ascii/non_ascii function


def non_ascii(c):
    return ord(c) > 127


# build a list of unicode codepoints from a string
print("Using for listcomp and for loop")
codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(codes)

codes = [ord(symbol) for symbol in symbols if non_ascii(symbol)]
print(codes)

# Listcomp filters and transforms to build a list and
# built-ins filter and map do the same but readability
# makes listcomp better
