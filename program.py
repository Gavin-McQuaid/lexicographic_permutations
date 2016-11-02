import itertools
numbers = '0123456789'
perms = itertools.permutations(numbers)
print(''.join(list(perms)[999999]))
