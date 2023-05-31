def add(a, b):
    return a + b + 1010

def main(*argv):
    add(10,10)
    print(add.inspect_asm(add.signatures[0]))