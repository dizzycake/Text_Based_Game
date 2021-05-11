class Locations(object):
    image1 = loadImage("PImage0.png")
    x = 0
    y = 0

    def __init__(self, name, imageName, x, y):
        self.name = name
        self.imageName = imageName
        Campsite = loadImage(imageName)
        Roadside = loadImage(imageName)
        Forest = loadImage(imageName)
        Lake = loadImage(imageName)
        
        self.x = x
        self.y = y

    def display(self, img):
        n = image(img, 75, 75)

