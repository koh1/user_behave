class User:
    
    def __init__(self, _id, name, homex, homey, officex, officey):
        self.id = _id
        self.name = name
        self.homex = homex
        self.homey = homey
        self.officex = officex
        self.officey = officey
        self.trace = []
        self.curx = homex
        self.cury = homey
        self.transport = None


    def initialize(self):
        self.trace = [[homex, homey]]
        self.curx = homex
        self.cury = homey

    def set_home(self, homex, homey):
        self.homex = homex
        self.homey = homey

    def set_office(self, officex, officey):
        self.officex = officex
        self.officey = officey
    
    def move_to(self,locx, locy):
        prev = [self.curx, self.cury]
        self.trace.append(prev)
        self.curx = locx
        self.cury = locy


    def dump(self):
        return {
            "name": self.name,
            "home": [self.homex, self.homey],
            "office": [self.officex, self.officey],
            "trace": self.trace
            }
