import sys

import numpy as np

from location import Location

class FieldMap:
    
    def __init__(self, width, height, unit, centers, center_extent):
        self.field_matrix = np.ones([width, height])
        self.locations = []
        self.stations = {}
        self.centers = []
        self.unit = unit
        for i in range(width):
            self.locations.append([])
            for j in range(height):
                self.locations[i].append(Location(i, j))

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
        
if __name__ == '__main__':
    fm = FieldMap(100, 100, 100, 5, 10)
    
    for i in range(100):
        line = ""
        for j in range(100):
            if fm.locations[i][j].center == True:
                line += str(1)
            else:
                line += str(0)
        
        print line


            
