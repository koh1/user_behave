import numpy as np
import pymongo
import datetime

from field_map import FieldMap
from location import Location
from user import User
from playground import PlayGround


class UserBehaveSim:
    
    def __init__(self, config):
        self.config = config
        self.logdb = pymongo.Connection(self.config['logdb']['db_host'], int(self.config['logdb']['db_port']))[self.config['logdb']['db_name']]
        self.prefix = '%s_%s' % (self.config['logdb']['prefix'], datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        self.pg = PlayGround(self.config['map'],
                             self.config['user'],
                             self.logdb, self.prefix)


    def run(self):
        total_sim_steps = int(self.config['sim']['total_sim_time_min'] / self.config['sim']['step_width_min'])
        prev_progress = 0
        for i in range(total_sim_steps):
            self.pg.process(i)
            progress = int((i * 100) / total_sim_steps)
            if progress > prev_progress:
                sys.stdout.write('Progress: %d%%\r' % progress)
                sys.stdout.flush()
                prev_progress = progress

        self.pg.flush_log()


if __name__ == '__main__':
    
    import yaml
    import sys

    params = sys.argv
    config = yaml.load(open(params[1]).read())
    ubs = UserBehaveSim(config)
    ubs.run()





