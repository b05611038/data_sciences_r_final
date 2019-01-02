import sys

from crawl.grabhistory import GrabHistory
#--------------------------------------------------------------------------------
#the crawl_process.py is the python file which can grab the data from the
#true highway database and pre-load for model training
#all the data in the database will be load in a long period of time, and it will
#be sort into different csv file for model training data grabbing
#the default path the data load is the root directory /csv, and the data will
#put inside and separated by different year, month and day
#--------------------------------------------------------------------------------#
if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('Please use the parameters correctly')

    gb = GrabHistory(from_year = int(sys.argv[1]))
    gb.grab()
