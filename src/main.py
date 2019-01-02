import sys

from traveltime.route import Route
from traveltime.traveltime import Ttime

from utils import *

if __name__ == '__main__':
    plan = Route('八堵交流道', '內湖交流道')
    plan.show()
