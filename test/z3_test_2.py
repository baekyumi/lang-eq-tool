from z3 import *

#0 == (x*(x+1)) % 2
#0 != (x*(x+1))%2

#x == (x+1-1)
#x == 2*x
#x != 2*x

#x != (x+1-1)

x = Int('x')
s = Solver()
print(s)
s.add(0 == (x*(x+1)) % 2)
print(s)
s.check()
print(s.check())

print()


"""
x = Int('x')
s2 = Solver()
print(s2)
s2.add(0 != (x*(x+1))%2)
print(s2)
s2.check()
print(s2.check())
"""
"""
s3 = Solver()
print(s3)
s3.add(x == (x+1-1))
print(s3)
s3.check()
print(s3.check())

print()

s4 = Solver()
print(s4)
s4.add(x == 2*x)
print(s4)
s4.check()
print(s4.check())

print()

s5 = Solver()
print(s5)
s5.add(x != 2*x)
print(s5)
s5.check()
print(s5.check())

print()

s6 = Solver()
print(s6)
s6.add(x != (x+1-1))
print(s6)
s6.check()
print(s6.check())
"""

'''
x = Int('x')
s2 = Solver()
print(s2)
s2.add(0 != (x*(x+1))%2)
print(s2)
s2.check()
print(s2.check())
'''