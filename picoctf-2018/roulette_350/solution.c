#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <limits.h>

int main() {
    int seed;
    printf("Seed: ");
    scanf("%d", &seed);
    srand(seed);
    for (int i = 0; i < 16; i++) {
        printf("predict: %d\n", (rand() % 36) + 1);
        rand();
    }
}

/*
The two bugs lie in the fact that get_long() may overflow and produce a negative number,
and that the randomness can be predicted.

Our initial amount of money is set as the seed for the prng, so we can use it to predict
which values we need to win any given round. However, we need to make use of the get_long() bug
to actually get to a value of 1 billion. We can do this by betting a negative number of money,
which will be subtracted from our balance, then intentionally lose the bet to keep it.

... 3 rounds of betting $1 and getting it right ...
How much will you wager?
Current Balance: $648    Current Wins: 3
> 3221225470
Choose a number (1-36)
> 1

Spinning the Roulette for a chance to win $2147483644!

Roulette  :  30

Not this time..
Stop wasting your time.

*** Current Balance: $1073742474 ***
picoCTF{1_h0p3_y0u_f0uNd_b0tH_bUg5_25142e09}

*/
