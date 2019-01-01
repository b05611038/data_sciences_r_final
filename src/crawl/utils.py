import datetime
import calendar
#--------------------------------------------------------------------------------
#the class and function are the basic function for crawling part
#--------------------------------------------------------------------------------
def get_time(mode):
    #the function to grab time of now
    #return the int of different mode
    #day: yy, mm, dd (3 ints list)
    #second: yy, mm, dd, hh, min, ss(6 ints list)
    now = datetime.datetime.now().isoformat()
    now = now.split('T')
    date = now[0].split('-')
    times = now[1].split('.')[0]
    times = times.split(':')
    if mode == 'day':
        return [int(i) for i in date]
    elif mode == 'second':
        return [int(i) for i in sum([date, times], [])]

def get_month_days(year, month):
    return calendar.monthrange(year, month)[1]


