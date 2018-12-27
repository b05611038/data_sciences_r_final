from crawl.grabhistory import GrabHistory
from crawl.grabnow import GrabNow

from dataprocessing.vehicledetector import VDdata
from dataprocessing.roadlevel import RLdata

from utils import *

if __name__ == '__main__':
    data = []
    test = RLdata('./data/roadlevel_value_2117.xml.gz', mode = 'no')
    data.append(test.grab())
    test = RLdata('./data/roadlevel_value_2118.xml.gz', mode = 'no')
    data.append(test.grab())
    test = RLdata('./data/roadlevel_value_2119.xml.gz', mode = 'no')
    data.append(test.grab())
    test = RLdata('./data/roadlevel_value_2120.xml.gz', mode = 'no')
    data.append(test.grab())
    test.printTitle()
    print(data[0][0])
    print(data[1][0])
    print(data[2][0])
    print(data[3][0])
