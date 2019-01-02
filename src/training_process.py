import sys

from crawl.grabhistory import GrabHistory

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
    if len(sys.argv) < 2:
        print('PLease put in the needed information correctly.')

    gb = GrabHistory(from_year = int(sys.argv[1]))
    gb.grab()

    info = RLInfo().grab()
    now = get_time('day') 
    for i in range(len(info)):
        routeid[info[i][0]] = info[i][5]
        try:
            worker = SVRtrain(info[i][0], [int(sys.argv[1])), 1, 1, now[0], now[1], now[2] - 1])
            worker.train()
            worker.save()
        except:
            print('Something wrong, skip training model: ' + info[i][5])


