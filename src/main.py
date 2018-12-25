from crawl.grabhistory import GrabHistory
from crawl.grabnow import GrabNow

from dataprocessing.roadlevel import RLone

if __name__ == '__main__':
    test = RLone('../../Downloads/roadlevel_value5_0100.xml.gz')
    data = test.grab()
    print(data[2])
