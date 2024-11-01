

doubler = lambda n: n * 2 
trippler = lambda n: n * 3

def multiplier(n):
    return lambda x: x * n

quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)


print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

print(trippler(8))
print(trippler(-4))
print(trippler('banana'))

print(quadrupler(4))
print(quadrupler(5))
print(sextupler(6))
print(septupler(7))
print(octupler(8))
print(nonupler(9))
print(decupler(10))