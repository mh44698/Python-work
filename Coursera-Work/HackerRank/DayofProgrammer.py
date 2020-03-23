

year = 2016

def dayOfProgrammer(year):
# Determine what day it falls on 256th day
    if is_leap(year) == True:
        #print("True")
        feb = 29
    else:
        feb = 28
    day = (256-(31+feb+31+30+31+30+31+31))
    print(f'{day}.09.{year}')
    return(f'{day}.09.{year}')

def is_leap(year):
    if year == 2100:
        return False
    if (year % 4 == 0 or year % 400 == 0) or year % 100 ==0:
        return True
    else:
        return False

dayOfProgrammer(year)
