#include <stdio.h>

#define NCOINS 8
int coins[NCOINS] = {1, 2, 5, 10, 20, 50, 100, 200};

int main()
{
    int i[8], cnt = 0;
    
    for (i[0] = 0; i[0] <= 200; ++i[0])
        for (i[1] = 0; i[1] <= 100; ++i[1])
            for (i[2] = 0; i[2] <= 40; ++i[2])
                for (i[3] = 0; i[3] <= 20; ++i[3])
                    for (i[4] = 0; i[4] <= 10; ++i[4])
                        for (i[5] = 0; i[5] <= 4; ++i[5])
                            for (i[6] = 0; i[6] <= 2; ++i[6])
                                for (i[7] = 0; i[7] <= 1; ++i[7])
                                    if (i[0]*coins[0] + i[1]*coins[1] + i[2]*coins[2] + 
                                        i[3]*coins[3] + i[4]*coins[4] + i[5]*coins[5] + 
                                        i[6]*coins[6] + i[7]*coins[7] == 200)
                                            cnt++;
    
    printf("%d\n", cnt);
    
    system("pause");
    return 0;
}
