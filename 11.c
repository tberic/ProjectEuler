#include <stdio.h>
#include <stdlib.h>

int a[20][20];

int main()
{
    FILE *in = fopen("11.txt", "rt");
    int i, j;
    long max;
    
    for (i = 0; i < 20; ++i)
        for (j = 0; j < 20; ++j)
            fscanf(in, "%d", &a[i][j]);
            
    max = 0L;
    //horizontal
    for (i = 0; i < 20; ++i)
        for (j = 0; j < 20 - 3; ++j)
            if ( a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3] > max)
                max = a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3];

    //vertical                     
    for (j = 0; j < 20; ++j)
        for (i = 0; i < 20 - 3; ++i)
            if ( a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j] > max)
                max = a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j];

    //diagonal
    for (i = 0; i < 20 - 3; ++i)
        for (j = 0; j < 20 - 3; ++j)
            if ( a[i][j]*a[i+1][j+1]*a[i+2][j+2]*a[i+3][j+3] > max)
                max = a[i][j]*a[i+1][j+1]*a[i+2][j+2]*a[i+3][j+3];

    //other diagonal
    for (i = 3; i < 20; ++i)
        for (j = 0; j < 20 - 3; ++j)
            if ( a[i][j]*a[i-1][j+1]*a[i-2][j+2]*a[i-3][j+3] > max)
                max = a[i][j]*a[i-1][j+1]*a[i-2][j+2]*a[i-3][j+3];

    printf("%ld\n", max);
    
    fclose(in);
    system("pause");
    return 0;
}
