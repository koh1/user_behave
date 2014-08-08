# -*- coding: utf-8 -*-

import sys

import numpy as np
from location import Location

class FieldMap:
    
    '''
    field_matrix
      1: normal
      2: center
      4: station
    '''

    def __init__(self, width, height, unit):
        self.width = width
        self.height = height
        self.field_matrix = np.ones([width, height])
        self.field_vector = np.arange(width * height)
        self.unit = unit
        self.centers = []
        self.stations = []

    def get_loc_in_center(self):
        return self.centers[np.random.randint(len(self.centers))]

    def get_loc_random(self):
        locint = self.field_vector[np.random.randint(len(self.field_vector))]
        row = int(locint / self.width)
        col = locint % self.width
        return [row, col]

    def place_centers(self, number, extent):
        for i in range(number):
            cx = int(np.random.randint(self.width))
            cy = int(np.random.randint(self.height))
            extent_width = int(extent / 2)
            if extent_width == 0:
                extent_width = 1
            
            for j in range(extent):
                cxj = cx - extent_width + j
                if cxj < 0 or cxj >= self.width:
                    continue
                for k in range(extent):
                    cyk = cy - extent_width + k
                    if cyk < 0 or cyk >= self.height:
                        continue

                    self.field_matrix[cxj][cyk] += 2
                    self.centers.append([cxj, cyk])

    def get_field_vector(self):
        pass

    def place_stations(self, number):
        map_nparry = np.array(self.map_matrix)
        nor = map_nparry.shape[0]
        noc = map_nparry.shape[1]
        target = np.arange(nor * noc)
        weight = map_nparry.reshape(nor * noc)
        weight *= 3
        weight += 1
        w_sum = np.sum(weight) 
        weight /= w_sum

        if np.sum(weight) > 1:
            weight[np.random.randint(len(weight))] -= np.sum(weight) - 1
        elif np.sum(weight) < 1:
            weight[np.random.randint(len(weight))] += 1 - np.sum(weight)
        

        stations = np.random.choice(target, number, replace=False, p=weight)

        for item in stations:
            row = item / noc
            col = item % noc
            
            self.locations[row][col].station = True
            self.map_matrix[row][col] += 2

if __name__ == '__main__':
    import pandas as pd
    import sys

    fm = FieldMap(100, 100, 100)

    for i in range(len(fm.field_matrix)):
        for j in range(len(fm.field_matrix[i])):
            sys.stdout.write("%s" % fm.field_matrix[i][j])
    
        sys.stdout.write("\n")

    fm.place_centers(10, 10)
    for i in range(len(fm.field_matrix)):
        for j in range(len(fm.field_matrix[i])):
            sys.stdout.write("%s" % fm.field_matrix[i][j])
    
        sys.stdout.write("\n")


