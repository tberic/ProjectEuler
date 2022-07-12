#include <stdio.h>

#define LEAP(m, y) ( (m == 2) && ( (y % 4 == 0) && (y % 100 != 0 || y % 400 == 0) ) )

int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int main()
{
    int day = 1, month = 1, year = 1901, dayofweek = 2;
    int cnt = 0;
    int d, m, y;
    
    d = 31;
    m = 12;
    y = 2000;
    
    while (year < y || month < m || day < d)
    {
        if (!dayofweek && day == 1)
        {
            cnt++;
            printf("%d %d\n", month, year);
        }
        
        dayofweek = (dayofweek + 1) % 7;
        day = day + 1;
        if (day > days[month-1] + LEAP(month, year))
        {
            day = 1;
            month++;
        }
        if (month > 12)
        {
            month = 1;
            year++;
        }        
    }
    
    printf("%d\n", cnt);
    //printf("%d\n", dayofweek);
    
    system("pause");
    return 0;
}
