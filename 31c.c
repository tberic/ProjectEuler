#include <stdio.h>

#define NCOINS 8
int coins[NCOINS] = {1, 2, 5, 10, 20, 50, 100, 200};
int cnt = 0;

int money(int x, int maxcoin)
{
    int i, sum = 0;

    if (maxcoin == 7)
        return 1;
        
    for (i = maxcoin; i < NCOINS; ++i)
    {
        if (x - coins[i] == 0) sum += 1;
        if (x - coins[i] > 0) sum += money(x-coins[i], i);
    }
    return sum;    
}

int main()
{
    printf("%d\n", money(200, 0));
    
    system("pause");
    return 0;
}
