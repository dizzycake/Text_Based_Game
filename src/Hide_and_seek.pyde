#Hide And Seek - Text Based Game
# by Joanna Bromka and Kate Nelson | 2021 Programming I

# TO DO LIST

#from Locations import Locations
from Characters import Characters

        
def setup():
    size(700, 500)
    global img, nessie
    nessie = Characters("nessie","Nessie.png", 75, 75)
    
    img = loadImage('Nessie.png')

    
def draw():
    background(0)
    rect(300, 200, 100, 100)
    nessie.display(img)
    
    
    
   
