import os
import numpy as np
import pandas as pd

from model.utils import *
#--------------------------------------------------------------------------------
#the dataloader python file is a python class which can cath all the data in the 
#csv file which we save our data
#all the info will be output as a numpy array in order to fit the datatype of the
#machine learning library sklearn for the tine regression problem
#--------------------------------------------------------------------------------
#class VDdataLoader():
#    def __init__(self):
    #suspension for the project need roadlevel data first

class RLdataLoader():
    def __init__(self, road_name, time_interval, data_dir = './csv', ram_limit = 4):
        #road_name is the para of the loaded road name, will bw catch by os lib
        self.road_name = road_name
        #pass in [start_year, start_month, start_day, end_year, end_month, end_day]
        self.time_interval = time_interval
        #the folder where we save the data, default is ./csv
        self.data_dir = data_dir

        #import the day feature from the csv file
        self.day_label = pd.read_csv(self.data_dir + '/label.csv')

        self.data = None
        self.label = None
        #control the batch of the data will not load exceed roughly 4G
        self.batch_size = self.ramLimit(ram_limit)

        self.build()

    def build(self):
        #return numpy array [train_data, train_target]
        #[cat(rl_value, rl_value5, features), time_travel]
        for year in range(self.time_interval[3], self.time_interval[0] - 1, -1):
            for month in range(12, 0, -1):
                for day in range(get_month_days(year, month), 0, -1):
                    if year == self.time_interval[3] and ((month > self.time_interval[4]) or (month == self.time_interval[4] and day > self.time_interval[5])):
                        continue

                    #the path where we store the training data
                    value_path = self.data_dir + '/' + str(year) + '/' + '%02d' % month + '/' + '%02d' % day + '/rl/' + self.road_name + '.csv'
                    value5_path = self.data_dir + '/' + str(year) + '/' + '%02d' % month + '/' + '%02d' % day + '/rl5/' + self.road_name + '.csv'

                    if self.data is None or self.data.shape[0] < self.batch_size:
                        if self.data is None and self.label is None:
                            try:
                                self.data, self.label = self.fileData(value_path, value5_path)
                            except:
                                continue
                        else:
                            try:
                                temp_data, temp_label = self.fileData(value_path, value5_path)
                                self.data = np.concatenate((self.data, temp_data), axis = 0)
                                self.label = np.concatenate((self.label, temp_label), axis = 0)
                                del temp_data, temp_label
                            except:
                                continue

                    else:
                        return       

                    if year == self.time_interval[0] and month == self.time_interval[1] and day == self.time_interval[2]:
                        break
                if year == self.time_interval[0] and month == self.time_interval[1]:
                    break
            if year == self.time_interval[0]:
                break

    def fileData(self, value_file, value5_file):
        #read the data by pandas lib indata is pd.dataframe
        value = pd.read_csv(value_file)
        value5 = pd.read_csv(value5_file)

        file_data = np.zeros((len(value_file) - 1, 108))
        file_label = np.zeros(len(value_file) - 1)
        for i in range(len(value_file) - 1):
            try:
                file_data[i] = self.batchData(value.iloc[i], value5.iloc[self.searchValue5(value.iloc[i, 0], value5)])
                file_label[i] = value.iloc[i + 1, 3]
            except:
                continue

        return file_data, file_label

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
        mini_batch = np.zeros(108)
        for i in range(1, len(value_line)):
            mini_batch[i - 1] = value_line.iloc[i]

        mini_batch[3: 51] = self.timeFeature(value_line.iloc[0])

        for i in range(1, len(value5_line)):
            mini_batch[50 + i] = value5_line.iloc[i]

        mini_batch[54: 102] = self.timeFeature(value5_line.iloc[0])
        mini_batch[102: 108] = self.dayFeature(value_line.iloc[0])

        return mini_batch

    def dayFeature(self, date_type):
        date_type = date_type.split(' ')[0]
        date_type = date_type.split('/')

        year = int(date_type[0])
        month = int(date_type[1])
        day = int(date_type[2])

        feature = np.zeros(6)
        label = -1
        for i in range(len(self.day_label)):
            if self.day_label.iloc[i, 0] == year and self.day_label.iloc[i, 1] == month and self.day_label.iloc[i, 2] == day:
                label = self.day_label.iloc[i, 3]

            if label > 0:
                feature[label - 1] = 1
                break

        return feature

    def timeFeature(self, input_time):
        #return the feature of length 48 one hot numpay array represent different times in a day
        input_time = input_time.split(' ')[1]
        input_time = input_time.split(':')
        hour = int(input_time[0])
        minute = int(input_time[1])
        feature = np.zeros(48)
        feature[2 * hour + int(minute / 30)] = 1
        
        return feature

    def ramLimit(self, setting):
        #calculated by one float 8 byte
        return int(setting * 1024 * 1024 * 1024 / (109 * 8))

class PredictLoader():
    def __init__(self, road_name, mode = 'rl', data_dir = './data'):
        #the predict dataloader is the class which grab the data from now
        #road_name is the road title we wants to predict
        self.road_name = road_name
        #the mode is the type which data we will use
        self.mode = mode
        #the data_dir is the directory class grabnow store file
        self.data_dir = self.data_dir
        #inherit by the brabnow class
        self.sub_title = ['roadlevel_value.xml.gz', 'roadlevel_value5.xml.gz', 'vd_value.xml.gz', 'vd_value5.xml.gz']

        self.data = None
        self.data = self.build(self.road_name)

    def build(self, road_name, mode):
        if mode == 'rl':
            batch_data = np.empty(108)
            grabber = RLdata(self.data_dir + '/' + self.self.sub_title[0])
            value = grabber.grab()
            grabber = RLdata(self.data_dir + '/' + self.self.sub_title[1])
            value5 = grabber.grab()

            for i in range(len(value)):
                if road_name == value[i][0]:
                    batch_data[0] = value[i][1]
                    batch_data[1] = value[i][2]
                    batch_data[2] = value[i][3]

                    batch_data[3: 51] = self.timeFeature(value[i][4])
                    
                    batch_data[51] = value5[i][1]
                    batch_data[52] = value5[i][2]
                    batch_data[53] = value5[i][3]

                    batch_data[54: 102] = self.timeFeature(value5[i][4])

                    batch_data[102: 108] = self.dayFeature(value[i][4])

                    return np.nan_to_num(batch_data.astype(np.float))
        else:
            return
            #still working

    def timeFeature(self, input_time):
        #return the feature of length 48 one hot numpay array represent different times in a day
        input_time = input_time.split(' ')[1]
        input_time = input_time.split(':')
        hour = int(input_time[0])
        minute = int(input_time[1])
        feature = np.zeros(48)
        feature[2 * hour + int(minute / 30)] = 1

        return feature.astype(np.float)

    def dayFeature(self, date_type):
        date_type = date_type.split(' ')[0]
        date_type = date_type.split('/')

        year = int(date_type[0])
        month = int(date_type[1])
        day = int(date_type[2])

        feature = np.zeros(6)
        label = -1
        for i in range(len(self.day_label)):
            if self.day_label.iloc[i, 0] == year and self.day_label.iloc[i, 1] == month and elf.day_label.iloc[i, 2] == day:
                label = self.day_label.iloc[i, 3]

            if label > 0:
                feature[label - 1] = 1
                break

        return feature


