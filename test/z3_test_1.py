from z3 import *

x = Int('x')
y = Int('y')
solve(x > 2, y < 10, x + 2 * y == 7)

print()

n = If(x+y >= 3, 2, 1)

print(n.num_args())
print(n.children())
print(n.arg(0))
print(n.decl())

print()

x = Real('x')
y = Real('y')
solve(x**2 + y**2 == 3, x**3 == 2)
set_option(precision = 30)
solve(x**2 + y**2 == 3, x**3 == 2)

print()

x = Int('x')
y = Int('y')
s = Solver()
print(s)
s.add(x > 10, y == x + 2)
print(s)
s.check()
print(s.check())
s.push()
s.add(y < 11)
print(s)
s.check()
print(s.check())
s.pop()
s.check()
print(s.check())

print()

x, y, z = Reals('x y z')
s = Solver()
s.add(x > 1, y > 1, x + y > 3, z - x < 10)
s.check()
print(s.check())

m = s.model()
for data in m.decls():
    print("%s = %s" %(data.name(), m[data]))


