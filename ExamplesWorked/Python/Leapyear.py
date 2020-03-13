year = int(input())

def is_leap(year):
    if year == 2100:
        return False
    if (year % 4 == 0 or year % 400 == 0) or year % 100 ==0:
        #print("Leap Year")
        return True
    else:
        #print("Non Leap Year")
        return False
is_leap(year)