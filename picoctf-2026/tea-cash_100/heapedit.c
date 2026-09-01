#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <inttypes.h>

#define CHUNK_COUNT 6
#define CHUNK_SIZE 0x80
#define FLAG_FILE "flag.txt"
#define FLAG_OFFSET (sizeof(void *))

static int is_known_chunk(void *p, void *chunks[], int n) {
    for (int i = 0; i < n; ++i) {
        if (chunks[i] == p) return 1;
    }
    return 0;
}
int main(void) {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    void *chunks[CHUNK_COUNT];
    char flag_buf[256] = {0};
    FILE *f = fopen(FLAG_FILE, "r");
    if (!f) {
        fprintf(stderr, "Could not open %s\n", FLAG_FILE);
        return 1;
    }
    if (!fgets(flag_buf, sizeof(flag_buf), f)) {
        fclose(f);
        fprintf(stderr, "Could not read flag from %s\n", FLAG_FILE);
        return 1;
    }
    fclose(f);

    size_t flen = strlen(flag_buf);
    if (flen && flag_buf[flen-1] == '\n') {
        flag_buf[flen-1] = '\0';
        flen--;
    }
    if (FLAG_OFFSET + flen >= CHUNK_SIZE) {
        fprintf(stderr, "Flag too large for chunk. Increase CHUNK_SIZE or reduce flag length.\n");
        return 1;
    }
    for (int i = 0; i < CHUNK_COUNT; ++i) {
        chunks[i] = malloc(CHUNK_SIZE);
        if (!chunks[i]) {
            fprintf(stderr, "malloc failed at i=%d\n", i);
            for (int j = 0; j < i; ++j) free(chunks[j]);
            return 1;
        }
        memset(chunks[i], 0, CHUNK_SIZE);
    }
    memcpy((char*)chunks[CHUNK_COUNT-1] + FLAG_OFFSET, flag_buf, flen + 1);
    void *head = chunks[0];
    printf("tcache head (start of free list) -> %p\n", head);
for (int i = CHUNK_COUNT - 1; i >= 0; --i) {
    free(chunks[i]);
}

    void *expected = head;
    for (int i = 0; i < CHUNK_COUNT; ++i) {
        void *user_addr = NULL;
        printf("Chunk %d address: ", i+1);
        if (scanf("%p", &user_addr) != 1) {
            fprintf(stderr, "Invalid input. Exiting.\n");
            return 1;
        }

        if (user_addr != expected) {
            fprintf(stderr, "Wrong address. Got %p. Exiting.\n", user_addr);
            return 1;
        }

        void *next = NULL;
        memcpy(&next, user_addr, sizeof(void *));

        if (next != NULL && !is_known_chunk(next, chunks, CHUNK_COUNT)) {
            fprintf(stderr, "Detected invalid next pointer value %p (not one of allocated chunks). Aborting to avoid crash.\n", next);
            fprintf(stderr, "Dump of first 16 bytes at %p: ", user_addr);
            unsigned char *b = user_addr;
            for (size_t z = 0; z < 16; ++z) {
                fprintf(stderr, "%02x ", b[z]);
            }
            fprintf(stderr, "\n");
            return 1;
        }

        expected = next;
    }
    char *flag_loc = (char*)chunks[CHUNK_COUNT-1] + FLAG_OFFSET;
    printf("Correct traversal! Flag: %s\n", flag_loc);

    return 0;
}
