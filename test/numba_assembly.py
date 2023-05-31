#!/usr/bin/env python

import math
import sys
import r2pipe
import numba

@numba.jit(nopython=True, nogil=True)
def add(a, b):
    return a + b + 1010

def main(*argv):
    add(10,10)
    print(add.inspect_asm(add.signatures[0]))

if __name__ == "__main__":
    rc = main(*sys.argv[1:])
    sys.exit(rc)


