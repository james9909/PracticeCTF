#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <limits.h>

static inline uint32_t rol(uint32_t u, size_t r) {
    __asm__ ("roll %1, %0" : "+g" (u) : "cI" (r));
    return u;
}

static inline uint32_t ror(uint32_t u, size_t r) {
    __asm__ ("rorw %1, %0" : "+g" (u) : "cI" (r));
    return u;
}

long replaceByte(char x, char n, char c) {
    int shift = (c << (8 * n));
    int mask = 0xFF << shift;
    return (~mask & x) | shift;
}

long to_long(char c1, char c2, char c3, char c4) {
    return (c1 << 0) | (c2 << 8) | (c3 << 16) | (c4 << 24);
}

int main() {
    char c[9] = {'p', 'i', 'c', 'o', 'C', 'T', 'F', '{'};
    for (int i = 0; i < 8 - 3; i++) {
        long value = to_long(c[i] ^ 0xDE, c[i+1], c[i+2], c[i+3]);
        printf("%x\n", value);
        break;
        value = ror(value, 0xD);
    }
    /* long intermediate = rol(c, 32 - 0xF); */
    /* intermediate = ror(intermediate & 0xFFFF, 16 - 0xD); */
    /* intermediate = (intermediate & 0xFF) ^ 0xDE; */
    /* printf("%x\n", intermediate); */

    int data[41] = {0xb1, 0xd3, 0x32, 0x4c, 0xfc, 0xe6, 0xef, 0x5e, 0xed, 0xe4, 0x66, 0xcd, 0x57, 0xf5, 0xe1, 0x7f, 0xcd, 0x7f, 0x55, 0xf6, 0xe9, 0x64, 0xe7, 0xc9, 0x7f, 0x75, 0xe9, 0x54, 0xe6, 0x4d, 0xf7, 0x79, 0xfc, 0xfc, 0x51, 0x71, 0xf9, 0x3e, 0x18, 0xd9, 0x00};
    /* int i = 0; */
    /* while (data[i] != 0) { */
    /*     printf("%d\n", rotate_left(rotate_right(data[i], 0xf), 0xd) ^ 0xde); */
    /*     i++; */
    /* } */
}
