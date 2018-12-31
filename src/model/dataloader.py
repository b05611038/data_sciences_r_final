import os
import numpy as np
import pandas as pd
#--------------------------------------------------------------------------------
#the dataloader python file is a python class which can cath all the data in the 
#csv file which we save our data
#all the info will be output as a numpy array in order to fit the datatype of the
#machine learning library sklearn for the tine regression problem
#--------------------------------------------------------------------------------
class VDdataLoader():
    #suspension for the project need roadlevel data first

class RLdataLoader():
    def __init__(self, road_name, time_interval, data_dir = './csv', ram_limit = 4):
        #road_name is the para of the loaded road name, will bw catch by os lib
        self.road_name = road_name
        #pass in [start_year, start_month, start_day, end_year, end_month, end_day]
        self.time_interval = time_interval
        #the folder where we save the data, default is ./csv
        self.data_dir = data_dir

        #control the batch of the data will not load exceed roughly 4G
        self.batch_size = self.ramLimit(ram_limit)

    def build(self, time_interval):
        #return numpy array [train_data, train_target]
        #[cat(rl_value, rl_value5, features), time_travel]
        for year in range(time_interval[3], time_interval[0] - 1, -1):
            for month in range(12, 0, -1):
                for day in range(get_month_days(year, month), 0, -1):
                    if year == time_interval[3] and ((month > time_interval[4]) or (month == time_interval[4] and day > time_interval[5])):
                        continue

                     #main code, not finish

                     if year == time_interval[0] and month == time_interval[1] and day == time_interval[2]:
                         break

            if year == time_interval[0] and month == time_interval[1]:
                break

        if year == time_interval[0]
            break
                    


    def fileData(self, value_file, value5_file):
        #read the data by pandas lib indata is pd.dataframe
        value = pd.read_csv(value_file)
        value5 = pd.read_csv(value5_file)

        file_data = np.empty((len(value_file) - 1, 102))
        for i in range(len(value_file) - 1):
            file_data[i] = self.batchData(value.iloc[i], value5.iloc[self.searchValue5(value.iloc[i, 0], value5)])

        return file_data

    def searchValue5(self, value_time, value5_dataframe):
        #return the index of value5
        flag = False
        for i in range(len(value5_dataframe) - 1):
            if value5_dataframe.iloc[i, 0] <= value_time and value5_dataframe.iloc[i + 1, 0] > value_time:
                flag = True

            if flag:
                return i

        return len(value5_dataframe) - 1

    def batchData(self, value_line, value5_line):
        #the function is used to concatenate the one mini-batch data
        mini_batch = np.empty(108)
        for i in range(1, len(value_line)):
            mini_batch[i - 1] = value_line.iloc[i]

        mini_batch[3: 51] = self.timeFeature(value_line.iloc[0])

        for i in range(1, len(value5_line)):
            mini_batch[50 + i] = value5_line.iloc[i]

        mini_batch[54: 102] = self.timeFeature(value5_line.iloc[0])
        mini_batch[102: 108] = self.dayFeature(value_line.iloc[0])

        return mini_batch.astype(np.float)

    def dayFeature(self, date_type):
        #not finish
        feature = np.zeros(6)
        feature[date_type] = 1

        return feature

    def timeFeature(self, input_time):
        #return the feature of length 48 one hot numpay array represent different times in a day
        input_time = input_time.split(' ')[1]
        input_time = input_time.split(':')
        hour = int(input_time[0])
        minute = int(input_time[1])
        feature = np.zeros(48)
        feature[2 * hour + int(minute / 30)] = 1
        
        return feature.astype(np.float)

    def ramLimit(self, setting):
        #calculated by one float 8 btye
        return int(setting * 1024 * 1024 * 1024 / (109 * 8))
