#include <stdio.h>

#define MAX(a,b) ( (a) > (b) ? (a) : (b) )
#define MAXN 100

int main()
{
    FILE *in = fopen("67.txt", "rt");
    int a[MAXN][MAXN];
    int s[MAXN][MAXN];
    int i, j;
    
    for (i = 0; i < MAXN; ++i)
        for (j = 0; j <= i; ++j)
            fscanf(in, "%d", &a[i][j]);

    for (i = MAXN-2; i >= 0; --i)
        for (j = 0; j <= i; ++j)
            a[i][j] = MAX(a[i][j] + a[i+1][j], a[i][j] + a[i+1][j+1]);
    
    printf("%d\n", a[0][0]);
    
    system("pause");
    return 0;
}
