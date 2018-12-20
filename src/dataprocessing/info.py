import os
import wget

from utils import *
from dataprocessing.utils import *
#--------------------------------------------------------------------------------
#the class and function used in process the info of the .xml file
#build the database for road dictionaray
#--------------------------------------------------------------------------------
class RLInfo():
    def __init__(self, files = './data/roadlevel_info.xml.gz', save_dir = './object'):
        #the class is going to build the info and dict of each roud interval of roadlevel info
        #grab the file from the data
        self.files = files
        self.save_dir = save_dir

        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        #to download the info file from the internet
        if not os.path.isfile(self.files):
            wget.download('http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz')

    def build(self):
        data = read_gz(self.files)
        data = data.split('\n')
        print(len(data))

#class VDInfo():
