#include <stdio.h>

int main() {
    int sum = 0;
    int x, y, z;
    for (x = 0; x < 687; x++) {
        for (y = 0; y < 687; y++) {
            for (z = 0; z < 687; z++) {
                if ((x + y + z) < 687) {
                    sum++;
                }
            }
        }
    }
    printf("%d\n", sum);
}

// $ gcc -O3 solution.c -o solution && ./solution
// 54276664
