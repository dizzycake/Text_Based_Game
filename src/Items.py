class Items:
    
   def __init__(self, name, imageName, x, y):
        self.name = name
        self.imageName = imageName
        self.x = x
        self.y = y 
        lamp = loadImage(imageName)
        tank = loadImage(imageName)
        photo = loadImage(imageName)
        snow = loadImage(imageName)
        cocoa = loadImage(imageName)
        
        def display(self, item):
            t = image(item, 400, 30)
