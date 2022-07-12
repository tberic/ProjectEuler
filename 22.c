#include <stdio.h>
#include <string.h>

#define MAXN 5163

int main()
{
    FILE *in = fopen("22.txt", "rt");
    char s[MAXN][100], tmp[100];
    int i, j;
    long sum = 0, sumt;
    
    for (i = 0; i < MAXN; ++i)
        fscanf(in, "%s", s[i]);

    for (i = 0; i < MAXN; ++i)
        for (j = i+1; j < MAXN; ++j)
            if ( strcmp(s[i], s[j]) > 0 )
            {
                strcpy(tmp, s[i]);
                strcpy(s[i], s[j]);
                strcpy(s[j], tmp);
            }
            
    for (i = 0; i < MAXN; ++i)
    {
        sumt = 0;
        for (j = 0; s[i][j] != 0; ++j)
            sumt += s[i][j] - 'A' + 1;
        sum += (i+1)*sumt;
    }

    printf("%ld\n", sum);            

    system("pause");
    return 0;
}
