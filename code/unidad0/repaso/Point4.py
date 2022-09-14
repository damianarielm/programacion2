from math import dist

class Point :
    ...

    def __sub__ (self, other ):
        return dist( (self.x, self.y), (other.x, other. y) )
