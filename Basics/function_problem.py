'''
    our task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given month/year pair (while only February is sensitive to the year value, your function should be universal).
'''

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
#
# Write your new code here.
#

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
