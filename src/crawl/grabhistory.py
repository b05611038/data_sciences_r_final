import os
import csv
import wget
import datetime

from src.utils import *
#--------------------------------------------------------------------------------
#the grabhistory.py is the setup file for new application model training
#--------------------------------------------------------------------------------
class GrabHistory():
    def __init__(self, path = './history', url = 'http://tisvcloud.freeway.gov.tw/history/'):
        #the path is to temporarily save the file for model training
        self.path = path

        #the item of nowadays date
        self.date = datetime.date.today().isoformat()

        #the url is used for the user re-train the predict model different from github release
        #the database is start from 2013
        self.url = url
        self.start_year = 2013

        #folder setup for the application
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def grab(self, year, month, day):

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
