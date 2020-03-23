# s = "07:05:45PM"
def timeConversion(s):
    hour = int(s[:2])
    meridian = s[8:]
    if (hour == 12):
        hour = 0
    if (meridian == 'PM'):
        hour += 12
    print("%02d" % hour + s[2:8])
    return("%02d" % hour + s[2:8])
    
timeConversion("07:05:45PM")
