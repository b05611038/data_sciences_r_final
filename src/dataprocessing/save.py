import os
import csv

from utils import *
from dataprocessing.utils import *
#--------------------------------------------------------------------------------
#the save.py is the python program to save the information of roadlevel and vd_value
# into a csv file
#--------------------------------------------------------------------------------
class RLStore():
    def __init__(self, data, save_path):
        #data is the data get from the database building training process
        #save_path means where the file need to be save
        #routeid, level, value, traveltime, datacollecttime
        self.data = data
        self.save_path = save_path
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        self.file_name = self.grabID(self.data)

    def save(self, all_info, filename_list):

    def writeFile(self, lines, filename):
        out_file = open(self.save_path + '/' + filename + '.csv', 'w')
        out_file.writelines(lines)
        outfile.close()

    def grabID(self, info):
        ID = []
        for i in range(len(info[0])):
            ID.append(info[0][i][0])

        return ID
