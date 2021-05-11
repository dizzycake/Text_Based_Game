#Hide And Seek - Text Based Game
# by Joanna Bromka and Kate Nelson | 2021 Programming I

# TO DO LIST

#from Locations import Locations
from Characters import Characters

        
def setup():
    size(700, 500)
    global img, img1, img2, img3, nessie, moth, bf, yeti, lamp, tank, photo, cocoa, snow
    
    # Characters 
    nessie = Characters("nessie","Nessie.png", 75, 75)
    img = loadImage('Nessie.png')
    moth = Characters("moth","MothMan.png", 75, 75)
    img = loadImage('MothMan.png')
    bf = Characters("bf","Big Foot.png", 75, 75)
    img = loadImage('Big Foot.png')
    yeti = Characters("yeti","Yeti.png", 75, 75)
    img = loadImage('Yeti.png')

    #Items/ Hiding places 
    lamp = Items("lamp", "Lampost.png", 75, 75 )
    l = loadImage('Lampost.png')
    
def draw():
     background(55)
    
    #nessie.display(img)
    #moth.display(img1)
    #bf.display(img2)
    #yeti.display(img3)
    
    lamp.display(item)
    
    
    #chatBox 
    strokeWeight(7)
    stroke(235, 237, 236)
    fill(0)
    rect(0,480, 900, 220 )
    
    #InteractBox 
    strokeWeight(7)
    stroke(235, 237, 236)
    fill(0)
    rect(0,0,300,480)
    
    
    
    
   
