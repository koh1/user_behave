import numpy as np

from field_map import FieldMap
from location import Location
from user import User
from playground import PlayGround


class UserBehaveSim:
    
    def __init__(self, config):
        self.config = config
        self.pg = PlayGround(self.config['map'],
                             self.config['user'])


    def run(self):
        total_sim_steps = int(self.config['sim']['total_sim_time_min'] / self.config['sim']['step_width_min'])
        for i in range(total_sim_steps):
            self.pg.process()


if __name__ == '__main__':
    
    import yaml
    import sys
    import pymongo
    
    params = sys.argv

    config = yaml.load(open(params[1]).read())
    ubs = UserBehaveSim(config)
    ubs.run()
    
    udump =ubs.pg.dump()
    print(udump)
    
#    col = pymongo.Connection('localhost', 27017)['test']['user']
#    col.insert(udump)





