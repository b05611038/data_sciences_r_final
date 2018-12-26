from crawl.grabhistory import GrabHistory
from crawl.grabnow import GrabNow

from dataprocessing.vehicledetector import VDdata

if __name__ == '__main__':
    test = VDdata('../../Downloads/vd_value_1828.xml.gz')
    test.printTitle()
    data = test.grab()
    print(len(data))
