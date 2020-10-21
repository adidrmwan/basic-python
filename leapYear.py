def is_leap(year):
    leap = False
    
    leap_year = year % 4
    leap_year_divided_100 = year % 100
    leap_year_divided_400 = year % 400



    if leap_year == 0:
        leap = True
        if leap_year_divided_100 == 0:
            leap = False
            if leap_year_divided_400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))