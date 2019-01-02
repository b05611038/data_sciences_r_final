from crawl.grabhistory import GrabHistory
from crawl.grabnow import GrabNow

from dataprocessing.vehicledetector import VDdata
from dataprocessing.roadlevel import RLdata
from dataprocessing.save import RLStore, VDStore

from traveltime.route import Route

from utils import *
import wget
if __name__ == '__main__':
    route = Route('八堵交流道', '內湖交流道')
    test = route.grab()
    print(test)
