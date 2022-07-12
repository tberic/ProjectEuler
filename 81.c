#include <stdio.h>

#define MIN(a,b) ( (a) < (b) ? (a) : (b) )

int main()
{
    FILE *in = fopen("81.txt", "rt");
    int i, j, n = 80;
    unsigned long a[80][80];
    
    for (i = 0; i < n; ++i)
        for (j = 0; j < n; ++j)
            fscanf(in, "%ld ", &a[i][j]);

    for (j = 1; j < n; ++j)
        a[0][j] += a[0][j-1];

    for (i = 1; i < n; ++i)
    {
        a[i][0] += a[i-1][0];
        for (j = 1; j < n; ++j)
            a[i][j] += MIN(a[i][j-1], a[i-1][j]);
    }
    
    printf("%ld\n", a[n-1][n-1]);    
    
    system("pause");
    fclose(in);
    return 0;
}
