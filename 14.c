#include <stdio.h>

#define MAXN 1000000L

int collatz(unsigned long x)
{
    int cnt = 0;
    while (x != 1)
    {
        if (x % 2 == 0)
            x = x/2;
        else
            x = 3*x + 1;
            
        cnt++;        
    }    
    
    return cnt;
}

int main()
{
    unsigned long i, maxi;
    int t, max = 0;
    
    for (i = 1; i < MAXN; i++)
    {
        t = collatz(i);
        if (t > max)
        {
            max = t;
            maxi = i;
        }
    }

    printf("%ld %ld\n", max, maxi);
    
    system("pause");    
    return 0;
}
