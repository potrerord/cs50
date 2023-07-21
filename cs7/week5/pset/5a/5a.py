"""
# Q1.1
y = set()
y.add('a')
y.add('a')
print(y)
"""

"""
# Q1.2
y = { 'b', 'a', 'b', 'c' }
y.remove('b')
print(y)
"""

"""
# Q1.3
y = { 'a', 'b' }
y.remove('c')
print(y)
"""

"""
# Q1.4
print('ab' in {'a', 'b', 'c'})
"""

"""
# Q2.1
y = {}
y['a'] = 2
y['b'] = 3
y['a'] = 4
print(y['a'])
print(y)
"""

"""
# Q2.2
y = {'a': 6, 'b': 1, 'c': 7}
y.pop('b')
print(y)
"""

"""
# Q2.3
y = {'a': 6, 'b': 7, 'c': 7}
y.pop('d')
print(y)
"""

"""
# Q2.4
y = {'a': 6, 'b': 7, 'c': 7}
for foo in y:
    print(foo)
"""

"""
# Q2.5
y = {'a': 6, 'b': 7, 'c': 7}
print('a' in y)
"""

"""
# Q2.6
y = {'a': 6, 'b': 7, 'c': 7}
print(6 in y)
"""

"""
# Q3.1
snacks = ["apple", "orange", "chocolate"]
mystery = [x + "s" for x in snacks]
print(mystery)
"""

# Q3.2
snacks = ['apple', 'orange', 'chocolate']
mystery = {x: len(x) for x in snacks}
print(mystery)




