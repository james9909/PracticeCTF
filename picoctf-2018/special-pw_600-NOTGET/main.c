#include <stdio.h>

extern int start(int argc, char** argv);

int main(int argc, char** argv) {
    printf("%x", start(argc, argv) & 0xff);
}
