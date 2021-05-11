#moth = loadImage("MothMan.png")

#bigf = loadImage("")
#yeti = loadImage("")

class Characters:
    #moth = loadImage("MothMan.png")
    #nessie = loadImage("Nessie.png")
    #x = 0
    #y = 0

    def __init__(self, name, imageName, x, y):
        self.name = name
        self.imageName = imageName
        nessie = loadImage(imageName)
        self.x = x
        self.y = y

    def display(self, img):
        n = image(img, 75, 75)

# MOTHMAN


# NESSY
    #nessie = Characters(self, self.nessie, self.nessie, 75, 75)

# BIGFOOT

# YETI
