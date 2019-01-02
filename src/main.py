import sys

from crawl.grabnow import GrabNow

from traveltime.route import Route
from traveltime.traveltime import Ttime

from utils import *

if __name__ == '__main__':
    gb = GrabNow()

    plan = Ttime('八堵交流道', '內湖交流道')
    plan.show()
