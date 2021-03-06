import datetime
import pickle
#--------------------------------------------------------------------------------
#the class and function are the basic function for running the application
#--------------------------------------------------------------------------------
def save_object(fname, obj):
    #the function is used to save some data in class or object in .pkl file
    with open(fname, 'wb') as out_file:
        pickle.dump(obj, out_file)
    out_file.close()

def load_object(fname):
    #the function is used to read the data in .pkl file
    with open(fname, 'rb') as in_file:
        return pickle.load(in_file)

def get_time(mode):
    #the function to grab time of now
    #return the int of different mode
    #day: yy, mm, dd (3 ints list)
    #second: yy, mm, dd, hh, min, ss(6 ints list)
    now = datetime.datetime.now().isoformat()
    now = now.split('T')
    date = now[0].split('-')
    times = now[1].split('.')[0]
    times = times.split(':')
    if mode == 'day':
        return [int(i) for i in date]
    elif mode == 'second':
        return [int(i) for i in sum([date, times], [])]

def timeFormat(string):
    text = string.split('/')
    for i in range(len(text)):
        text[i] = int(text[i])

    return text
