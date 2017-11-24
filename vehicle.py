class Vehicle:
    def __init__(self, _id, name, fromx, fromy, tox, toy):
        self.id = _id
        self.name = name
        self.fromx = fromx
        self.fromy = fromy
        self.tox = tox
        self.toy = toy
        self.trace = [[fromx, fromy]]
        self.curx = fromx
        self.cury = fromy

    def move_to(self, locx, locy):
        prev = [self.curx, self.cury]
        self.trace.append(prev)
        self.curx = locx
        self.cury = locy


    def dump(self):
        return {
            "name": self.name,
            "from": [self.fromx, self.fromy],
            "to": [self.tox, self.toy],
            "trace": self.trace
            }
