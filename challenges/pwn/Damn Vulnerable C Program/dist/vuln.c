#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void win_function() {
    printf("Congratulations! Here's your flag: YCEP24{REDACTED}\n");
}

void vulnerable_function() {
    char buffer[64];
    gets(buffer); // This is a vulnerable function
}

int main(int argc, char **argv) {
    vulnerable_function();
    return 0;
}
