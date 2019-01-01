from crawl.grabhistory import GrabHistory
from crawl.grabnow import GrabNow

from model.model import *
from model.dataloader import *
from model.utils import *

from dataprocessing.info import *

from utils import *
#--------------------------------------------------------------------------------
#the grab_training_data.py is the python file which can grab the data from the
#true highway database and pre-load for model training
#all the data in the database will be load in a long period of time, and it will
#be sort into different csv file for model training data grabbing
#the default path the data load is the root directory /csv, and the data will
#put inside and separated by different year, month and day
#--------------------------------------------------------------------------------
if __name__ == '__main__':
    #gb = GrabHistory(from_year = 2018)
    #gb.grab()

    gn = GrabNow()
    gn.update()

    info = RLInfo().grab()
    routeid = {}
    for i in range(len(info)):
        routeid[info[i][0]] = info[i][5]
        worker = SVRtrain(info[i][0], [2018, 1, 1, 2018, 6, 23])
        worker.train()
        worker.save()

    save_object('./data/refer.pkl', routeid)


