#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *in = fopen("8.txt", "rt");
    char s[10000];
    int i, max;
    
    fscanf(in, "%s", s);
    
    max = 0;
    for (i = 0; s[i+4] != 0; ++i)
        if ((s[i]-'0')*(s[i+1]-'0')*(s[i+2]-'0')*(s[i+3]-'0')*(s[i+4]-'0') > max)
            max = (s[i]-'0')*(s[i+1]-'0')*(s[i+2]-'0')*(s[i+3]-'0')*(s[i+4]-'0');
    
    printf("%d\n", max);
        
    fclose(in);
    system("pause");
    return 0;
}
