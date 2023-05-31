from z3 import *

# Variable declaration used to compare registers
a = Int('a')
b = Int('b')

# Solver Declaration for Comparison
s = Solver()

# EAX Register to compare found in numba_miasm result
# EAX = ECX_init + EDX_init + 0x3F2

# EAX Register to compare found in c_miasm result
# EAX = @32[@32[call_func_stack(0x11C5, ESP_init)] + 0x8] + @32[@32[call_func_stack(0x11C5, ESP_init)] + 0xC]

# Add condition with replacing randomly assigned registers with variable names assigned above
s.add((a + b + 0x3F2) != (a + b + 0x3F2))
print(s)
print(s.check())

