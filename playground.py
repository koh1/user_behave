import numpy as np


from field_map import FieldMap
from user import User


class PlayGround:
    
    def __init__(self, map_config, user_config):
        self.fm = FieldMap(map_config['width'],
                           map_config['height'],
                           map_config['unit_meter'])

        self.fm.place_centers(map_config['center']['num'],
                              map_config['center']['extent'])

        self.user_dists = []
        self.users = []
        for i in range(int(user_config['num'])):
            h = self.fm.get_loc_random()
            o = self.fm.get_loc_in_center()
            u = User(i, "user_%07d" % i, h, o)
            self.users.append(u)

    def dump(self):
        r = []
        for u in self.users:
            r.append(u.dump())
        return r

    def process(self):
        for u in self.users:
            self.move_user(u)

    def move_user(self, u):
        attractions = self.calc_attractions_proto(u)
        sel_arry = self.direction_select_array(attractions)
        direction = sel_arry[np.random.randint(len(sel_arry))]
        
        if direction == 0: ## NORTH
            u.move_to([u.current_loc[0], u.current_loc[1]+1])

        elif direction == 1: ## EAST
            u.move_to([u.current_loc[0]+1, u.current_loc[1]])

        elif direction == 2: ## SOUTH
            u.move_to([u.current_loc[0], u.current_loc[1]-1])

        elif direction == 3: ## WEST
            u.move_to([u.current_loc[0]-1, u.current_loc[1]])
    
    def calc_attractions_proto(self, user):
        '''
        no user specific attraction
        [north, east, south, west]の配列を返す
        '''
        x = user.current_loc[0]
        y = user.current_loc[1]
        
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


