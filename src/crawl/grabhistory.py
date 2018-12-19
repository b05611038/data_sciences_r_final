import os
import csv
import wget
import datetime

from utils import *
#--------------------------------------------------------------------------------
#the grabhistory.py is the setup file for new application model training
#--------------------------------------------------------------------------------
class GrabHistory():
    def __init__(self, path = '../history', save_dir = '../data', url = 'http://tisvcloud.freeway.gov.tw/history'):
        #the path is to temporarily save the file for model training
        self.path = path
        self.save_dir = save_dir

        #the item of nowadays date
        self.date = datetime.date.today().isoformat()

        #the url is used for the user re-train the predict model different from github release
        #the database is start from 2013
        self.url = url
        self.start_year = 2013

        #folder setup for the application
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def grab(self):
        now = get_time('day')
        datatype = ['/vd', '/roadlevel']
        for i in range(len(datatype)):
            for year in range(self.start_year, (now[0] + 1)):
                for month in range(1, 13):
                    for day in range(1, (get_month_days(year, month) + 1)):
                        for hour in range(24):
                            for minute in range(60):
                                download_url = self.url + datatype[i] + '/' + str(year) + '%02d' % month + '%02d' % day + datatype[i] + '_value_' + '%02d' % hour + '%02d' % minute + '.xml.gz'
                                wget.download(download_url, out = (self.save_dir + '/' + str(year) + '%02d' % month + '%02d' % day + datatype[i].replace('/', '') + '_value_' + '%02d' % hour + '%02d' % minute + '.xml.gz'))
                                if hour == 23 and minute == 56:
                                    break

                            for minute in range(0, 60 , 5):
                                download_url = self.url + datatype[i] + '/' + str(year) + '%02d' % month + '%02d' % day + datatype[i] + '_value5_' + '%02d' % hour + '%02d' % minute + '.xml.gz'
                                wget.download(download_url, out = (self.save_dir + '/' + str(year) + '%02d' % month + '%02d' % day + datatype[i].replace('/', '') + '_value5_' + '%02d' % hour + '%02d' % minute + '.xml.gz'))
                                if hour == 23 and minute == 45:
                                    break

                        if year == now[0] and month == now[1] and day == (now[2] - 1):
                            break
                    if year == now[0] and month == now[1]:
                        break
                if year == now[0]:
                    break

    def modelLatest(self):
        #return true or false for check the model history
        if not os.path.exists(self.path + '/model_date.txt'):
            #means the model is first time update
            return False
        else:
            f = open(self.path + '/model_date.txt', 'r')
            last = f.read()
            f.close()
            return self.date == last

    def updateLatest(self):
        if not os.path.exists(self.path + '/model_date.txt'):
            #first time create model_date.txt
            f = open(self.path + '/model_date.txt', 'w')
            f.writelines(datetime.date.today().isoformat())
            f.close()
        else:
            os.remove(self.path + '/model_date.txt')
            f = open(self.path + '/model_date.txt', 'w')
            f.writelines(datetime.date.today().isoformat())
            f.close()
