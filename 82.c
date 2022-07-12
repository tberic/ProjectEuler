#include <stdio.h>

#define MIN2(a,b) ( (a) < (b) ? (a) : (b) )
#define MIN(a,b,c) ( (a) < (b) ? (MIN2(a,c)) : (MIN2(b,c)) )

int main()
{
    FILE *in = fopen("82.txt", "rt");
    int i, j, n = 80;
    unsigned long a[80][80][2];
    unsigned long min;
    
    for (i = 0; i < n; ++i)
        for (j = 0; j < n; ++j)
        {
            fscanf(in, "%ld ", &a[i][j][0]);
            a[i][j][1] = a[i][j][0];
        }

    for (j = 1; j < n; ++j)
    {
        a[0][j][1] += MIN2(a[0][j-1][0], a[0][j-1][1]);
        for (i = 1; i < n; ++i)
            a[i][j][1] += MIN(a[i][j-1][0], a[i][j-1][1], a[i-1][j][1]);

        a[n-1][j][0] += MIN2(a[n-1][j-1][0], a[n-1][j-1][1]);
        for (i = n-2; i >= 0; --i)
            a[i][j][0] += MIN(a[i][j-1][0], a[i][j-1][1], a[i+1][j][0]);        
    }

/*
    for (i = 0; i < n; ++i)
    {
        for (j = 0; j < n; ++j)
            printf("%d ", MIN2(a[i][j][0],a[i][j][1]));
        printf("\n");
    }
*/    
    min = MIN2(a[0][n-1][0], a[0][n-1][1]);
    for (i = 0; i < n; ++i)
        if (MIN2(a[i][n-1][0], a[i][n-1][1]) < min)
            min = MIN2(a[i][n-1][0], a[i][n-1][1]);

    printf("%ld\n", min);
    
    system("pause");
    fclose(in);
    return 0;
}
