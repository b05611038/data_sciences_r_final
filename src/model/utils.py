import calendar
#--------------------------------------------------------------------------------
#the utils.py put the function which will used in the model part of the programe
#--------------------------------------------------------------------------------
def get_month_days(year, month):
    return calendar.monthrange(year, month)[1]
