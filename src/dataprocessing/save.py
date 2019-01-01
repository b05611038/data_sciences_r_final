import os
import csv

from utils import *
from dataprocessing.utils import *
#--------------------------------------------------------------------------------
#the save.py is the python program to save the information of roadlevel and vd_value
# into a csv file
#--------------------------------------------------------------------------------
class RLStore():
    def __init__(self, data, save_path, verbose = 0):
        #data is the data get from the database building training process
        #save_path means where the file need to be save
        #routeid, level, value, traveltime, datacollecttime
        self.data = data
        self.save_path = save_path
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        #default is 0, won't see any verbose information
        self.verbose = verbose

        self.file_name = self.grabID(self.data)
        self.save(self.data, self.file_name)

    def save(self, all_info, filename_list):
        for i in range(len(all_info[0])):
            lines = ['datacollecttime,level,value,traveltime\n']
            for j in range(len(all_info)):
                try:
                    lines.append(str(all_info[j][i][4]) + ',' + str(all_info[j][i][1]) + ',' + str(all_info[j][i][2]) + ',' + str(all_info[j][i][3]) + '\n')
                except:
                    continue

            self.writeFile(lines, filename_list[i])

            if self.verbose != 0:
                print('Progress: ', i + 1, ' / ', len(filename_list), ', Writing file ', filename_list[i], '.csv done')

    def writeFile(self, lines, filename):
        out_file = open(self.save_path + '/' + filename + '.csv', 'w')
        out_file.writelines(lines)
        out_file.close()

    def grabID(self, all_info):
        ID = []
        for i in range(len(all_info[0])):
            ID.append(all_info[0][i][0])

        return ID

class VDStore():
    def __init__(self, data, save_path, verbose = 0):
        #data is the data get from the database building training process
        #save_path means where the file need to be save
        #vdid, status, datacollecttime, [vsrdir, vsrid, speed, laneoccupy, carS volume, carT volume, carL volume]
        self.data = data
        self.save_path = save_path
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        #default is 0, won't see any verbose information
        self.verbose = verbose

        self.file_name = self.grabID(self.data)
        self.save(self.data, self.file_name)

        print('All progress done')

    def save(self, all_info, filename_list):
        for i in range(len(all_info[0])):
            lines = ['datacollecttime,status,vsrdir,vsrid,speed,laneoccupy,carS volume,carT volume,carL volume,...\n']
            for j in range(len(all_info)):
                try:
                    lines_temp = ''
                    lines_temp = str(all_info[j][i][2]) + ',' + str(all_info[j][i][1]) + ','
                    for k in range(3, len(all_info[j][i])):
                        lines_temp += str(all_info[j][i][k][0]) + ',' + str(all_info[j][i][k][1]) + ',' + str(all_info[j][i][k][2]) + ',' + str(all_info[j][i][k][3]) + ',' + str(all_info[j][i][k][4]) + ',' + str(all_info[j][i][k][5]) + ',' + str(all_info[j][i][k][6])

                        if k == len(all_info[j][i]) - 1:
                            lines_temp += '\n'
                        else:
                            lines_temp += ','

                    lines.append(lines_temp)
                except:
                    continue

            self.writeFile(lines, filename_list[i])

            if self.verbose != 0:
                print('Progress: ', i + 1, ' / ', len(filename_list), ', Writing file ', filename_list[i], '.csv done')

    def writeFile(self, lines, filename):
        out_file = open(self.save_path + '/' + filename + '.csv', 'w')
        out_file.writelines(lines)
        out_file.close()

    def grabID(self, all_info):
        ID = []
        for i in range(len(all_info[0])):
            ID.append(all_info[0][i][0])

        return ID


