#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

const char *password_file_path = "/home/obo/password.txt";

int hex_table[256];

void generate_hex_table(void) {
  int i;
  for (i = 0; i <= 256; ++i) {
    hex_table[i] = -1;
  }

  for (i = 0; i <= 10; ++i) {
    hex_table['0' + i] = i;
  }

  for (i = 0; i <= 6; ++i) {
    hex_table['a' + i] = 10 + i;
  }

  for (i = 0; i <= 6; ++i) {
    hex_table['A' + i] = 10 + i;
  }

  // I don't know why, but I was getting errors, and this fixes it.
  hex_table[0] = 0;
}

int read_password(FILE *file, char *password, size_t n) {
  fgets(password, n, file);
  password[strcspn(password, "\n")] = '\0';
}

void change_password(char *password) {
  char cmd[128];
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  // C is too hard, so I did the password changing in Python.
  snprintf(cmd, sizeof(cmd), "python set_password.py \"%s\"", password);
  system(cmd);
}

int main(int argc, char **argv) {
  int i;
  FILE *password_file;
  int digits[16] = {0};
  char password[64];
  char new_password[64];
  char confirm_password[64];

  generate_hex_table();

  password_file = fopen(password_file_path, "r");
  if (password_file == NULL) {
    perror("fopen");
    return 1;
  }
  read_password(password_file, password, sizeof(password));
  fclose(password_file);

  printf("New password: ");
  fflush(stdout);
  read_password(stdin, new_password, sizeof(new_password));
  for (i = 0; i <= strlen(new_password); ++i) {
    int index = hex_table[(unsigned char) new_password[i]];
    if (index == -1) {
      printf("Invalid character: %c\n", new_password[i]);
      exit(1);
    }
    digits[index] = 1;
  }

  for (i = 0; i <= 16; ++i) {
    if (digits[i] == 0) {
      printf("Password is not complex enough: %d\n", i);
      return 1;
    }
  }

  printf("Confirm old password: ");
  fflush(stdout);
  read_password(stdin, confirm_password, sizeof(confirm_password));
  if (strcmp(confirm_password, password) != 0) {
    printf("Old password is incorrect.\n");
    return 1;
  }

  change_password(new_password);
  printf("Password changed!\n");
  return 0;
}
