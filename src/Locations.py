class Locations(object):
    image1 = loadImage("PImage0.png")
    x = 0
    y = 0
    
    def __init__(self):
        x = 10
        y = 10

    def display(self):
        image(self.image1, self.x, self.y)
        point(self.x, self.y)


# CAMPSITE

# FOREST

# LAKE

# CAVE

# ROADSIDE
