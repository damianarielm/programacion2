class Rectangle(Polygon):
    def area (self):
        A = self.vertices[0]
        E = self.vertices[1]
        B = self.vertices[2]
        D = self.vertices[4]
        base = B - E
        altura = B - D
        return base * altura
