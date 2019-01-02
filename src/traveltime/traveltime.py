import os

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
        self.times = get_time(mode = 'second')
        self.route = self.showRoute(self.start, self.target)

    def predictTime(self, route, now):
        #the main part of the project
        #route and now are python list with it needed object
        

    def model(self, model_name):
        #the predict process of each model
        loader = PredictLoader(model_name)
        data = loader.data

        model = SVRmodel(self.model_dir + '/' + model_name + '.pkl')
        times = model.predict(data)

        return times

    def showRoute(self, start, target):
        #return all the road intervl we need to go
        plan = Route(start, target)
        route = plan.grab()
        return route


