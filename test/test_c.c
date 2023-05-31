#include <stdio.h>

// int add(int a, int b) memory location : 0x1190
int add(int a, int b) {
    return a + b + 1010;
}
void main() {
    add(10,10);
}


