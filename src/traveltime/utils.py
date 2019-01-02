import calendar
import datetime
#--------------------------------------------------------------------------------
#the utils.py is used in the process of predict time interval
#--------------------------------------------------------------------------------
def get_month_days(year, month):
    return calendar.monthrange(year, month)[1]

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

def timeToString(times):
    #will convert time list to string
    return str(times[0]) + '-' + '%02d' % times[1] + '-' + '%02d' % times[2] + 'T' + '%02d' % times[3] + ':' + '%02d' % times[4] + ':' + '%02d' % times[5]

def secondString(times, display = 5):
    #will convert seconds to minutes or hour
    intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
    )

    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:display])
