# """1.1"""

# y = ['a', 'b', 'c']
# y[2] = 'd'
# print(y)

# """1.2"""

# y = ['a', 'b', 'c']
# y.append('d')
# print(y)


# """1.3"""

# y = ['a', 'b', 'a']
# y.remove('a')
# print(y)

# """1.4"""

# y = ['a', 'b', 'c']
# y.insert(2, 'a')
# print(y)
#

"""2.1"""
foobar = [1, 4, 9, 16, 25]
length = len(foobar)
foobar_shifted = []


for i in range(length):
    foobar_shifted.append(foobar[(i - 1) % length])

foobar = foobar_shifted
print(foobar)


"""2.2"""




"""2.3"""




"""2.4"""



