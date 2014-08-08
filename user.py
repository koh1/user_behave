class User:
    
    def __init__(self, _id, name, home, office):
        self.id = _id
        self.name = name
        self.home = [home[0],home[1]]
        self.office = [office[0],office[1]]
        self.trace = []
        self.current_loc = [home[0], home[1]]
        self.transport = None


    def initialize(self):
        self.trace = [home]
        self.current_loc = home

    def set_home(self, home):
        self.home = home

    def set_office(self, office):
        self.office = office
    
    def move_to(self,location):
        prev = [self.current_loc[0], self.current_loc[1]]
        self.trace.append(prev)
        self.current_loc = location


    def dump(self):
        return {
            "name": self.name,
            "home": [self.home[0],self.home[1]],
            "office": [self.office[0], self.office[1]],
            "trace": self.trace
            }
