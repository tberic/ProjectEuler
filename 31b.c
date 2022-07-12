#include <stdio.h>

#define NCOINS 8
int coins[NCOINS] = {200, 100, 50, 20, 10, 5, 2, 1};

int main()
{
    int i[7], cnt = 0;
    
    for (i[0] = 200; i[0] >= 0; i[0] -= coins[0])
    for (i[1] = i[0]; i[1] >= 0; i[1] -= coins[1])
    for (i[2] = i[1]; i[2] >= 0; i[2] -= coins[2])
    for (i[3] = i[2]; i[3] >= 0; i[3] -= coins[3])
    for (i[4] = i[3]; i[4] >= 0; i[4] -= coins[4])
    for (i[5] = i[4]; i[5] >= 0; i[5] -= coins[5])
    for (i[6] = i[5]; i[6] >= 0; i[6] -= coins[6])
        cnt++;
    
    printf("%d\n", cnt);
    
    system("pause");
    return 0;
}
