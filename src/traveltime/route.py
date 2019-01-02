import os
import csv

from dataprocessing.info import *

from utils import *
from traveltime.utils import *
#--------------------------------------------------------------------------------
#the route.py will provide the connection of each part of the highway
#--------------------------------------------------------------------------------
class Route():
    def __init__(self, start, target, road_ref = './csv/roadlevel_info.xml.gz'):
        #the route class is the map of the highway, will provide the middle route from start to target
        self.start = start
        self.target = target

        #road_ref is teh reference of each route which is already sorted
        self.road_ref = road_ref
        self.route_order = self.maps(self.road_ref)
        self.route = self.plan(self.start, self.target, self.route_order)

    def grab(self):
        return self.route

    def plan(self, start, target, maps):
        #return the middle part of the road in order
        route = []
        index = [-1, -1]
        for i in range(len(maps)):
            if maps[i][3] == start:
                index[0] = i
            if maps[i][3] == target:
                index[1] = i

        index.sort()
        for indexs in range(index[0], index[1] + 1):
            route.append(maps[indexs][0])

        return route

    def maps(self, ref):
        #[[routeid, road_level, start, end]]
        grabber = RLInfo(files = ref)
        info = grabber.grab()

        map_info = []
        for i in range(len(info)):
            map_info.append(self.extract(info[i]))

        return map_info

    def extract(self, line_info):
        #extract the information from a list returned by roadlevel info
        lines = []
        #routeid
        lines.append(line_info[0])

        text = line_info[5][::-1].replace(')', '', 1)
        text = text[::-1].split('(', 1)

        #freeway number one
        lines.append(text[0])
        text = text[1]
        text = text.split('到')

        lines.append(text[0])
        lines.append(text[1])

        return lines


