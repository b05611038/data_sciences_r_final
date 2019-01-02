import sys

from crawl.grabhistory import GrabHistory

from model.model import *
from model.dataloader import *
from model.utils import *

from dataprocessing.info import *

from utils import *
#--------------------------------------------------------------------------------
#the train_process.py is the python file for taining the model of the data which
# is grabbed by the crawl_process.py. The model we used in the project is SVR, the
#accurate model for regression.
#--------------------------------------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('PLease put in the needed information correctly.')

    info = RLInfo().grab()
    start = timeFormat(sys.argv[1])
    end = timeFormat(sys.argv[2])
    for i in range(len(info)):
        try:
            worker = SVRtrain(info[i][0], [start[0], start[1], start[2], end[0], end[1], end[2]], int(sys.argv[3]))
            worker.train()
            worker.save()
        except:
            print('Something wrong, skip training model: ' + info[i][5])


