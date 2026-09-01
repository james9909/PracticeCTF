#include <stdio.h>
#include <stdlib.h>

/*
This is not the challenge, just a template to answer the questions.
To get the flag, answer all the questions. 
There are no bugs in the quiz.
There are 0xD questions in total.

*/

void win(){
        system("cat flag.txt");
}

void vuln(){
        char buffer[0x15] = {0};
        fprintf(stdout, "\nEnter payload: ");
        fgets(buffer, 0x90, stdin);
}

void main(){
        vuln();
}
