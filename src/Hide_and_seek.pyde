#Hide And Seek - Text Based Game
# by Joanna Bromka and Kate Nelson | 2021 Programming I

# TO DO LIST

#from Locations import Locations
from Characters import Characters

        
def setup():
    size(700, 500)
    global img, nessie, moth, bf, yeti
    
    # Characters 
    nessie = Characters("nessie","Nessie.png", 75, 75)
    img = loadImage('Nessie.png')
    moth = Characters("moth","MothMan.png", 75, 75)
    img = loadImage('MothMan.png')
    bf = Characters("bf","Big Foot.png", 75, 75)
    img = loadImage('Big Foot.png')
    yeti = Characters("yeti","Yeti.png", 75, 75)
    img = loadImage('Yeti.png')

    
def draw():
    background(0)
    rect(300, 200, 100, 100)
    nessie.display(img)
    #moth.display(img)
    #bf.display(img)
    #yeti.display(img)
    
    
    
   
