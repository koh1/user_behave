# -*- coding: utf-8 -*-

import sys

import numpy as np
from location import Location

class FieldMap:
    
    def __init__(self, width, height, unit, centers, center_extent):
        self.field_matrix = np.ones([width, height])
        self.locations = []
        self.map_matrix = []
        self.stations = {}


        self.unit = unit
        for i in range(width):
            self.locations.append([])
            self.map_matrix.append([])
            for j in range(height):
                self.locations[i].append(Location(i, j))
                self.map_matrix[i].append(0)

        
        ## 中心街の生成
        for i in range(centers):
            cx = np.random.randint(width)
            cy = np.random.randint(height)
            extent_width = center_extent / 2
            if extent_width == 0:
                extent_width = 1
            
            for j in range(center_extent):
                cxj = cx - extent_width + j
                if cxj < 0 or cxj >= width:
                    continue
                for k in range(center_extent):
                    cyk = cy - extent_width + k
                    if cyk < 0 or cyk >= height:
                        continue
                    
                    self.locations[cxj][cyk].center = True
                    self.map_matrix[cxj][cyk] = 1



        self.place_stations(1000)
                    
    def place_stations(self, number):
        map_nparry = np.array(self.map_matrix)
        nor = map_nparry.shape[0]
        noc = map_nparry.shape[1]
        target = np.arange(nor * noc)
        weight = map_nparry.reshape(nor * noc)
        weight *= 3
        weight += 1
        vlen = np.linalg.norm(weight)
        weight /= vlen

        stations = self.random_choice(target, weight, number)
        
        for item in stations:
            row = item / noc
            col = item % noc
            
            self.locations[row][col].station = True
            self.map_matrix[row][col] += 2

        
    def random_choice(self, arry, weight, num):
        if len(arry) <= num:
            return arry

        if len(weight) <= num:
            return arry

        counter = 0
        pointer = 0
        result = []
#        tmp_arry = np.copy(arry)
#        np.random.shuffle(tmp_arry)
        mv = np.amax(arry)
        while counter < num:
            rand = np.random.random()*mv
            if rand < weight[pointer]:
                result.append(arry[pointer])
                print arry[pointer]
                counter += 1

        return result
        
if __name__ == '__main__':

    import pandas as pd
    fm = FieldMap(100, 100, 100, 10, 5)
    nparry = np.array(fm.map_matrix)
    
    
    print np.amax(nparry)

    '''
    for i in range(100):
        line = ""
        for j in range(100):
            if fm.locations[i][j].center == True:
                line += str(1)
            else:
                line += str(0)
        
        print line
     '''
            
