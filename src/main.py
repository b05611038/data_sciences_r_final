import sys

from crawl.grabnow import GrabNow

from traveltime.traveltime import Ttime

from utils import *
#--------------------------------------------------------------------------------
#this is the main of user for freeway travel time prediction. The program can make
#user input the start place and the target they wants to go, and the program will
#output the route they need to go, and output time they need
#--------------------------------------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please check the input is all correct')

    gb = GrabNow()
    gb.update()

    plan = Ttime(sys.argv[1], sys.argv[2])
    plan.show()
