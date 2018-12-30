from crawl.grabhistory import GrabHistory
from crawl.grabnow import GrabNow

from dataprocessing.vehicledetector import VDdata
from dataprocessing.roadlevel import RLdata
from dataprocessing.save import RLStore, VDStore

from utils import *
import wget
if __name__ == '__main__':
    gb = GrabHistory(from_year = 2018)
    gb.grab()
