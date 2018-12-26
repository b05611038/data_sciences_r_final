import os

from utils import *
from dataprocessing.utils import *
#--------------------------------------------------------------------------------
#the vehicledectector.py is the class which grab the data from the vd_value.xml
#include one minutes and five minutes
#--------------------------------------------------------------------------------
class VDdata():
    def __init__(self, file_path, mode = 'remove'):
        self.file_path = file_path
        #the path of the vd_value info
        #five minutes and one minute is all share this grab data class

        self.mode = mode
        #default is remove: remove the input file after grab the data from file

        self.title = ['vdid', 'status', 'datacollecttime', ['vsrdir', 'vsrid', 'speed' , 'laneoccupy', 'carS volume', 'carT volume', 'carL volume']]

        self.data = []

        self.build()

        #default mode is remove, will not store file in the folder
        if mode == 'remove':
            os.remove(self.file_path)

    def build(self):
        text = read_gz(self.file_path)
        text = text.split('Infos')
        text = text[1].split('/Info')
        for i in range(len(text) - 1):
            self.data.append(self.blockInfo(text[i]))

    def grab(self):
        if len(self.data) != 0:
            return self.data
        else:
            print('Something wrong, plaease check the path of the folder')

    def grabTitle(self):
        return self.title

    def printTitle(self):
        print('vdid, status, datacollecttime, [vsrdir, vsrid, speed, laneoccupy, carS volume, carT volume, carL volume]')

    def blockInfo(self, inString):
        info = []
        inString = inString.split('lane')
        vdtitle = inString[0].split('"')
        for i in range(1, 6, 2):
            info.append(vdtitle[i])

        for i in range(1, len(inString), 3):
             sub_info = []
             sub_text_one = inString[i]
             sub_text_two = inString[i + 1]

             sub_text_one = sub_text_one.split('"')
             for j in range(1, 6, 2):
                 sub_info.append(sub_text_one[j])

             sub_text_two = sub_text_two.split('"')
             for j in range(1, 14, 4):
                 sub_info.append(sub_text_two[j])

             info.append(sub_info)

        return info
