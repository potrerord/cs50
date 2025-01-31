# 1.1
y = ['a', 'b', 'c']
y[2] = 'd'
print(y)


# 1.2
y = ['a', 'b', 'c']
y.append('d')
print(y)


# 1.3
y = ['a', 'b', 'a']
y.remove('a')
print(y)


# 1.4
y = ['a', 'b', 'c']
y.insert(2, 'a')
print(y)


# 2.1
foobar = [-1, 4, -9, 16, -25]
foobar = [5 for _ in foobar]
print(foobar)

# 2.2
foobar = [-1, 4, -9, 16, -25]
foobar = foobar[-1:] + foobar[:-1]
print(foobar)

# 2.3
foobar = [-1, 4, -9, 16, -25]
foobar[0], foobar[-1] = foobar[-1], foobar[0]
print(foobar)

# 2.4
foobar = [-1, 4, -9, 16, -25]
foobar = [abs(element) for element in foobar]
print(foobar)
