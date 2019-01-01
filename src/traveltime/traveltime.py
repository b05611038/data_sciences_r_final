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
    def __init__(self, start, target):
        #the start and the target is the where we need to travel on the highway
        self.start = start
        self.target = target

        #the list of time right now
        self.times = get_time(mode = 'second')

    def predictTime(self):
        #the main part of the project

    def showRoute(self): 
