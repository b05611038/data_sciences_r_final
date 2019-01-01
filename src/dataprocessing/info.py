import os
import wget

from utils import *
from dataprocessing.utils import *
#--------------------------------------------------------------------------------
#the class and function used in process the info of the .xml file
#build the database for road dictionaray
#--------------------------------------------------------------------------------
class RLInfo():
    def __init__(self, files = './data/roadlevel_info.xml.gz'):
        #the class is going to build the info and dict of each roud interval of roadlevel info
        #grab the file from the data
        self.files = files
        self.title = ['routeid', 'sourceid', 'locationpath', 'startlocationpoint', 'endlocationpoint', 'roadsection', 'roadtype', 'fromkm', 'tokm', 'speedlimit']
        self.info = []

        #to download the info file from the internet
        if not os.path.isfile(self.files):
            wget.download('http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz')

        self.build()

    def build(self):
        data = read_gz(self.files)
        data = data.split('\n')
        for i in range(3, len(data) - 3):
            self.info.append(self.lineInfo(data[i]))

    def grab(self):
        if len(self.info) == 0:
            print('Please check the file and the path setting')
            return None
        else:
            return self.info

    def grabTitle(self):
        return self.title

    def printTitle(self):
        print('routeid, sourceid, locationpath, startlocationpoint, endlocationpoint, roadsection, roadtype, fromkm, tokm, speedlimit')

    def lineInfo(self, inString):
        #return list[routeid, sourceid, locationpath, startlocationpoint, endlocationpoint, roadsection, roadtype, fromkm, tokm, speedlimit]
        info = []
        inString = inString.split('"')
        for i in range(1, 20, 2):
            info.append(inString[i])

        return info
        
class VDInfo():
    def __init__(self, files = './data/vd_info.xml.gz'):
        #the class is going to build the info and dict of each roud interval of roadlevel info
        #grab the file from the data
        self.files = files
        self.save_dir = save_dir
        self.info = []
        self.title = ['vdid', 'routeid', 'roadsection', 'locationpath', 'startlocationpoint', 'endlocationpoint', 'roadway', 'vsrnum', 'vdtype', 'locationtype', 'px', 'py']

        #to download the info file from the internet
        if not os.path.isfile(self.files):
            wget.download('http://tisvcloud.freeway.gov.tw/vd_info.xml.gz')

        self.build()

    def build(self):
        data = read_gz(self.files)
        data = data.split('\n')
        for i in range(3, len(data) - 3):
            self.info.append(self.lineInfo(data[i]))

    def grab(self):
        if len(self.info) == 0:
            print('Please check the file and the path setting')
            return None
        else:
            return self.info

    def grabTitle(self):
        return self.title

    def printTitle(self):
        print('vdid, routeid, roadsection, locationpath, startlocationpoint, endlocationpoint, roadway, vsrnum, vdtype, locationtype, px, py')

    def lineInfo(self, inString):
        #return list[vdid, routeid, roadsection, locationpath, startlocationpoint, endlocationpoint, roadway, vsrnum, vdtype, locationtype, px, py]
        info = []
        inString = inString.split('"')
        for i in range(1, 24, 2):
            info.append(inString[i])

        return info


