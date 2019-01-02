import os
import numpy as np

import sklearn
from sklearn.svm import SVR

from model.utils import *
from model.dataloader import *
from utils import *
#--------------------------------------------------------------------------------
#the train.py is the train class of the support vector regression in order to 
#improve the preformance of the true highway time prediction
#--------------------------------------------------------------------------------
class SVRtrain():
    def __init__(self, road_name, time_interval, C, save_dir = './model_weight', mode = 'rl'):
        #road_name is the para that the road range we want to training
        self.road_name = road_name
        #time interval is the para we need to pass in dataloader
        #pass in [start_year, start_month, start_day, end_year, end_month, end_day]
        self.time_interval = time_interval
        #save_dir is where we save the model, default is ./model_weight
        self.save_dir = save_dir
        #mode is dertermine that the model's traninig data we use, default is 'rl'
        self.mode = mode

        #C is the parameter of SVR model
        self.C = C

        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        self.model = SVR(gamma = 0.001, C = self.C, verbose = True)

    def train(self):
        #the mode will have three mode for different traininig data, but still working
        if self.mode == 'rl':
            dataloader = RLdataLoader(self.road_name, self.time_interval, ram_limit = 32)

        train_x = dataloader.data
        train_y = dataloader.label
        del dataloader

        train_x = np.nan_to_num(train_x).astype(np.float)
        train_y = np.nan_to_num(train_y) .astype(np.float)

        print('Finish data loading, Start training SVRmodel for road name ' + self.road_name)

        self.model.fit(train_x, train_y)

    def save(self):
        save_object(self.save_dir + '/' + self.road_name + '.pkl', self.model)

class SVRmodel():
    def __init__(self, model):
        if type(model) == str:
            #menas the model is from the path
            self.model = load_object(model)
        elif type(model) == sklearn.svm.classes.SVR:
            self.model = model
        else:
            print('Please check your model')
            return

    def predict(self, info):
        return self.model.predict(info)


