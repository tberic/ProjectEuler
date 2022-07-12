#include <stdio.h>
#include <math.h>

int main()
{
    FILE *in = fopen("99.txt", "rt");
    int i, j, t, a[1000], b[1000], oa[1000], ob[1000];
    
    for (i = 0; i < 1000; ++i)
    {
        fscanf(in, "%d,%d\n", &a[i], &b[i]);
        oa[i] = a[i];
        ob[i] = b[i];
    }
        
    for (i = 0; i < 1000; ++i)
        for (j = i+1; j < 1000; ++j)
            if (b[i] < b[j]*(double)log(a[j])/(double)log(a[i]))
            {
                t = a[i]; a[i] = a[j]; a[j] = t;
                t = b[i]; b[i] = b[j]; b[j] = t;
            }
    printf("%d, %d\n", a[0], b[0]);
    
    for (i = 0; i < 1000; ++i)
        if (oa[i] == a[0] && ob[i] == b[0])
            printf("%d\n", i);
    
    system("pause");
    fclose(in);
    return 0;
}

