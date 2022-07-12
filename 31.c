#include <stdio.h>

#define NCOINS 8
int coins[NCOINS] = {1, 2, 5, 10, 20, 50, 100, 200};

int main()
{
    int i, j, k;
    int comb[201] = {0};
    
    for (j = 0; j < NCOINS; ++j)
        comb[coins[j]] = 1;
    
    for (i = 1; i <= 200; ++i)
        for (j = 0; coins[j] < i; ++j)
            comb[i] += comb[i-coins[j]];
    
    printf("%d %d %d %d %d\n", comb[1], comb[2], comb[3], comb[4], comb[5]);
    printf("%d\n", comb[200]);
    
    system("pause");
    return 0;
}
