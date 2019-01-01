import os
import wget
import datetime

from utils import *
from crawl.utils import *
#--------------------------------------------------------------------------------
#the grabnow.py is the setup file of app opening
#--------------------------------------------------------------------------------
class GrabNow():
    def __init__(self, save_dir = './data', url = 'http://tisvcloud.freeway.gov.tw/'):
        #the directory of the data is the folder the app will save the information of now
        self.save_dir = save_dir

        #the url is the link which can download the information from the government website
        self.url = url

        #the time when the app initial the class
        self.latest = datetime.datetime.now().isoformat().split(':')
        self.latest = self.latest[0] + self.latest[1]

        #the filename need to download
        self.sub_title = ['roadlevel_value.xml.gz', 'roadlevel_value5.xml.gz', 'vd_value.xml.gz', 'vd_value5.xml.gz']

        #folder setup for the application
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        #grab the information in the initial
        self.remove()
        self.grab()

    def update(self):
        now = datetime.datetime.now().isoformat().split(':')
        now = now[0] + now[1]
        if now > self.latest:
            self.remove()
            self.grab()
            self.latest = now

    def grab(self):
        for i in range(len(self.sub_title)):
            download_url = self.url + self.sub_title[i]
            wget.download(download_url, out = (self.save_dir + '/' + self.sub_title[i]))

    def remove(self):
        file_list = os.listdir(self.save_dir)
        for files in file_list:
            os.remove(self.save_dir + '/'+ files)


