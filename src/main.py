from crawl.grabhistory import GrabHistory
from crawl.grabnow import GrabNow

from dataprocessing.vehicledetector import VDdata
from dataprocessing.roadlevel import RLdata
from dataprocessing.save import RLStore, VDStore

from utils import *

if __name__ == '__main__':
    data = []
    test = VDdata('./data/vd_value_0928.xml.gz', mode = 'no')
    data.append(test.grab())
    test = VDdata('./data/vd_value_2352.xml.gz', mode = 'no')
    data.append(test.grab())
    test = VDdata('./data/vd_value_2353.xml.gz', mode = 'no')
    data.append(test.grab())
    test = VDdata('./data/vd_value_2354.xml.gz', mode = 'no')
    data.append(test.grab())

    action = VDStore(data, './csv')
