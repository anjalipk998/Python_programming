def is_year_leap(year):
    if(year%4==0&year%100!=0):
        return True
    elif(year%400==0):
        return True
    return False

def days_in_month(year, month):
    days =None
    thirtyoneDays=[1,3,5,7,8,10,12]
    thirtyDays=[4,6,9,11]
    for elm in thirtyoneDays:
        if(elm==month):
            days=31
            return days
    for elm in thirtyDays:
        if(elm==month):
            days=30
            return days
    if(month==2):
        if(is_year_leap(year)):
            days=29
        else:
            days=28
    return days

def day_of_year(year, month, day):
    dayCalculated=days_in_month(year,month)
    if(day==dayCalculated):
        return True
    else:
        return None


print(day_of_year(2000, 12, 31))
