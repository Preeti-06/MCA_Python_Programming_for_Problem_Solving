from point import Point

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def show(self):
        print("Center:", self.center.x, self.center.y)
        print("Radius:", self.radius)