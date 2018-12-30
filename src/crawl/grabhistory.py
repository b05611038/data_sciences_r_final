import os
import csv
import wget
import datetime

from utils import *
from crawl.utils import *

from dataprocessing.vehicledetector import VDdata
from dataprocessing.roadlevel import RLdata
from dataprocessing.save import RLStore, VDStore
#--------------------------------------------------------------------------------
#the grabhistory.py is the setup file for new application model training
#--------------------------------------------------------------------------------
class GrabHistory():
    def __init__(self, from_year = 2013, path = './history', save_dir = './csv'):
        #the path is to temporarily save the file for model training
        self.path = path
        self.save_dir = save_dir
        self.datatypes = ['/vd', '/vd5', '/rl', '/rl5']

        #the item of nowadays date
        self.date = datetime.date.today().isoformat()

        #the url is used for the user re-train the predict model different from github release
        #the database is start from 2013
        self.url = 'http://tisvcloud.freeway.gov.tw/history'
        self.start_year = 2013
        self.from_year = from_year
        if self.from_year < self.start_year:
            self.from_year = self.start_year

        #folder setup for the application
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        
        for year in range(self.from_year, get_time('day')[0] + 1):
            if not os.path.exists(self.save_dir + '/' + str(year)):
                os.makedirs(self.save_dir + '/' + str(year))

            for month in range(1, 13):
                if not os.path.exists(self.save_dir + '/' + str(year) + '/' + '%02d' % month):
                    os.makedirs(self.save_dir + '/' + str(year) + '/' + '%02d' % month)

                for day in range(1, (get_month_days(year, month) + 1)):
                    if not os.path.exists(self.save_dir + '/' + str(year) + '/' + '%02d' % month + '/' + '%02d' % day):
                        os.makedirs(self.save_dir + '/' + str(year) + '/' + '%02d' % month + '/' + '%02d' % day)

                    for i in range(len(self.datatypes)):
                        if not os.path.exists(self.save_dir + '/' + str(year) + '/' + '%02d' % month + '/' + '%02d' % day + self.datatypes[i]):
                            os.makedirs(self.save_dir + '/' + str(year) + '/' + '%02d' % month + '/' + '%02d' % day + self.datatypes[i])

    def grab(self):
        now = get_time('day')
        datatype = ['/vd', '/roadlevel']
        for i in range(len(datatype)):
            for year in range(self.from_year, (now[0] + 1)):
                for month in range(1, 13):
                    for day in range(1, (get_month_days(year, month) + 1)):
                        value = []
                        value5 = []
                        for hour in range(24):
                            for minute in range(60):
                                download_url = self.url + datatype[i] + '/' + str(year) + '%02d' % month + '%02d' % day + datatype[i] + '_value_' + '%02d' % hour + '%02d' % minute + '.xml.gz'
                                wget.download(download_url, out = './temp.xml.gz')

                                try:
                                    if i == 0:
                                        grabber = VDdata('./temp.xml.gz')
                                    elif i == 1:
                                        grabber = RLdata('./temp.xml.gz')

                                except:
                                    os.remove('./temp.xml.gz')
                                    continue                                

                                value.append(grabber.grab())

                                if hour == 23 and minute == 56:
                                    break
                            
                            for minute in range(0, 60 , 5):
                                download_url = self.url + datatype[i] + '/' + str(year) + '%02d' % month + '%02d' % day + datatype[i] + '_value5_' + '%02d' % hour + '%02d' % minute + '.xml.gz'
                                wget.download(download_url, out = './temp.xml.gz')

                                try:
                                    if i == 0:
                                        grabber = VDdata('./temp.xml.gz')
                                    elif i == 1:
                                        grabber = RLdata('./temp.xml.gz')

                                except:
                                    os.remove('./temp.xml.gz')
                                    continue

                                value5.append(grabber.grab())

                                if hour == 23 and minute == 45:
                                    break
                        if i == 0:
                            saver = VDStore(value, self.save_dir + '/' + str(year) + '/' + '%02d' % month + '/' + '%02d' % day + self.datatypes[0])
                            saver = VDStore(value5, self.save_dir + '/' + str(year) + '/' + '%02d' % month + '/' + '%02d' % day + self.datatypes[1])
                        elif i == 1:
                            saver = RLStore(value, self.save_dir + '/' + str(year) + '/' + '%02d' % month + '/' + '%02d' % day + self.datatypes[2])
                            saver = RLStore(value5, self.save_dir + '/' + str(year) + '/' + '%02d' % month + '/' + '%02d' % day + self.datatypes[3])
                        del value, value5
                        print('%02d' % year, '%02d' % month, '%02d' % day, ' done')

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
