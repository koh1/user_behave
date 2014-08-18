# -*- coding: utf-8 -*-

import numpy as np
import time


from field_map import FieldMap
from user import User

class PlayGround:
    
    def __init__(self, map_config, user_config, logdb, prefix):

        self.fm = FieldMap(int(map_config['width']),
                           int(map_config['height']),
                           int(map_config['unit_meter']),
                           logdb, prefix)

        self.fm.place_centers(int(map_config['center']['num']),
                              int(map_config['center']['extent']))

        self.fm.dump_map()

        self.user_dists = []
        self.users = []
        self.users_on_map = np.zeros((int(map_config['width']),
                                     int(map_config['height'])))
        for i in range(int(user_config['num'])):
            h = self.fm.get_loc_random()
            o = self.fm.get_loc_in_center()
            u = User(i, "user_%07d" % i, h[0], h[1], o[0], o[1])
            self.users.append(u)
            self.users_on_map[u.curx][u.cury] += 1
        
        self.logdb = logdb['%s_udist' % prefix]
            
        self.logging_buff_size = 10
        self.logging_buff = []

    def dump_user_dist(self):
        r = []
        for i in range(self.fm.width):
            for j in range(self.fm.height):
                r.append([i, j, self.users_on_map[i][j]])

        return r

    def process(self, step_count):
        for u in self.users:
            self.move_user(u)

        log = {"time": step_count,
               "dist": self.dump_user_dist()}
        self.logging(log, False)
    
    def flush_log(self):
        if len(self.logging_buff) > 0:
            self.logdb.insert(self.logging_buff)
            self.logging_buff = []

    def logging(self, data, flush):
        self.logging_buff.append(data)
        if len(self.logging_buff) >= self.logging_buff_size or flush:
           self.logdb.insert(self.logging_buff) 
           self.logging_buff = []

    def move_user(self, u):
        attractions = self.calc_attractions_proto(u)
        sel_arry = self.direction_select_array(attractions)
        direction = sel_arry[np.random.randint(len(sel_arry))]
        self.users_on_map[u.curx][u.cury] -= 1        
        if direction == 0: ## NORTH
            self.users_on_map[u.curx][u.cury+1] += 1
            u.move_to(u.curx, u.cury+1)

        elif direction == 1: ## EAST
            self.users_on_map[u.curx+1][u.cury] += 1
            u.move_to(u.curx+1, u.cury)

        elif direction == 2: ## SOUTH
            self.users_on_map[u.curx][u.cury-1] += 1
            u.move_to(u.curx, u.cury-1)

        elif direction == 3: ## WEST
            self.users_on_map[u.curx-1][u.cury] += 1
            u.move_to(u.curx-1, u.cury)
    
    def calc_attractions_proto(self, user):
        '''
        no user specific attraction
        [north, east, south, west]の配列を返す
        '''
        x = user.curx
        y = user.cury
        
        if y < self.fm.height - 1:
            yp = self.fm.field_matrix[x][y+1]
        else:
            yp = 0
        if x < self.fm.width - 1:
            xp = self.fm.field_matrix[x+1][y]
        else:
            xp = 0
        if y > 0:
            ym = self.fm.field_matrix[x][y-1]
        else:
            ym = 0
        if x > 0:
            xm = self.fm.field_matrix[x-1][y]
        else:
            xm = 0
        return [yp, xp, ym, xm]
        
    def direction_select_array(self, attr_arry):
        r = []
        for i in range(len(attr_arry)):
            for j in range(int(attr_arry[i])):
                r.append(i)
        return r


