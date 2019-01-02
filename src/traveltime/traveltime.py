import os
import datetime

from model.model import *
from model.dataloader import *

from crawl.grabnow import *

from traveltime.route import *

from traveltime.utils import *
from utils import *
#--------------------------------------------------------------------------------
#the class is used in the main.py as the most important part of the project
#--------------------------------------------------------------------------------
class Ttime():
    def __init__(self, start, target, model_dir = './model_weight'):
        #the start and the target is the where we need to travel on the highway
        self.start = start
        self.target = target

        #the directory is where we stored our model
        self.model_dir = model_dir

        #the list of time right now
        self.timeReset()
        self.route, self.way = self.showRoute(self.start, self.target)

    def show(self):
        print('Now times: ' + datetime.datetime.now().isoformat().split('.')[0])

        print('Start predict the times...')
        spend = self.predictTime(self.route)

        print('You will go through: ')

        for i in range(len(self.way)):
            print(self.way[i])

        print('\nYou are going to arrive at ' + timeToString(self.time))
        print('All times about ' + secondString(spend))

    def predictTime(self, route):
        #the main part of the project
        #route and now are python list with it needed object
        self.timeReset()
        cumulated_time = 0
        for i in range(len(route)):
            time_temp = self.model(route[i], self.time)
            cumulated_time += time_temp
            self.timeIter(time_temp)

        return cumulated_time

    def timeIter(self, plus):
        #plus parameter second
        self.time[5] += plus
        add = 0
        if self.time[5] >= 60:
            add = self.time[5] / 60
            self.time[5] = self.time[5] % 60
            self.time[4] += add

        add = 0
        if self.time[4] >= 60:
            add = self.time[4] / 60
            self.time[4] = self.time[4] % 60
            self.time[3] += add

        add = 0
        if self.time[3] >= 24:
            add = self.time[3] / 24
            self.time[3] = self.time[3] % 24
            self.time[2] += add

        add = 0
        if self.time[2] >= get_month_days(self.time[0], self.time[1]):
            add = self.time[2] / get_month_days(self.time[0], self.time[1])
            self.time[2] = self.time[2] % get_month_days(self.time[0], self.time[1])
            self.time[1] += add

        add = 0
        if self.time[1] >= 12:
            add = self.time[1] / 12
            self.time[1] = self.time[1] % 12
            self.time[0] += add            

    def timeReset(self):
        self.time = get_time(mode = 'second')

    def model(self, model_name, times):
        #the predict process of each model
        loader = PredictLoader(model_name, now = times)
        data = loader.data

        model = SVRmodel(self.model_dir + '/' + model_name + '.pkl')
        spend_time = model.predict(data)

        return spend_time

    def showRoute(self, start, target):
        #return all the road intervl we need to go
        plan = Route(start, target)
        route = plan.grab()
        way = plan.grabWay()
        return route, way


