#include <stdio.h>

int main() {
    printf("%d", asm3(0xbda42100,0xb98dd6a5,0xecded223));
}

/*
$ gcc -masm=intel -m32 solution.c end_asm_rev.S
$ ./a.out
1144 (or 0x478 in he)
*/
