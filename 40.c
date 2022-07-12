#include <stdio.h>

#define MAXN 1000000L

int digit(long n, int k)
{
    char s[20];
    
    ltoa(n, s, 10);
    return s[k]-'0';
}

int main()
{
    long i, n, s = 0, goal = 1;
    int prod = 1;
    int e;
        
    for (s = 1, n = 1, e = 1; goal <= MAXN; n *= 10, e++)
        for (i = n; i < n*10; ++i)
        {
            if (goal <= s && s < goal + e)
            {
                prod *= digit(i, s-goal);
                goal *= 10;
            }
            s += e;
        }
    
    printf("%d\n", prod);
    
    system("pause");
    return 0;
}
