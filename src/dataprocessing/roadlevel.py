import os

from utils import *
from dataprocessing.utils import *
#--------------------------------------------------------------------------------
#the roadlevel.py is the class which grab the data from the roadlevel.xml
#include one minutes and five minutes
#--------------------------------------------------------------------------------
class RLdata():
    def __init__(self, file_path, mode = 'remove'):
        self.file_path = file_path
        #the path of the roadlevel info
        #five minutes and one minute is all share this grab data class

        self.mode = mode
        #default is remove: remove the input file after grab the data from file

        self.title = ['routeid', 'level', 'value', 'traveltime', 'datacollecttime']

        self.data = []

        self.build()

        #default mode is remove, will not store file in the folder
        if mode == 'remove':
            os.remove(self.file_path)

    def build(self):
        text = read_gz(self.file_path)
        text = text.split('\n')
        for i in range(3, len(text) - 3):
            self.data.append(self.lineInfo(text[i]))

    def grab(self):
        if len(self.data) != 0:
            return self.data
        else:
            print('Something wrong, plaease check the path of the folder')

    def grabTitle(self):
        return self.title

    def printTitle(self):
        print('routeid, level, value, traveltime, datacollecttime')

    def lineInfo(self, inString):
        info = []
        inString = inString.split('"')
        for i in range(1, 10, 2):
            info.append(inString[i])

        info[1] = int(info[1])
        info[2] = int(info[2])
        info[3] = int(info[3])

        return info
