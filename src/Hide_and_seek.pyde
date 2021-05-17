#Hide And Seek - Text Based Game
# by Joanna Bromka and Kate Nelson | 2021 Programming I

# TO DO LIST

#Needed fpr keypressed
Answer1 = False
Answer2 = False
Answer3 = False

NessieReaction1 = False
NessieReaction2 = False
NessieReaction3 = False

#from Locations import Locations
from Characters import Characters

        
def setup():
    size(900, 700)
    global img, img1, img2, img3, nessie, moth, bf, yeti, camp, forest, lake, cave, road, loc, loc1, loc2, loc3, loc4
    global lamp, tank, photo, snow, cocoa, tem, tem1, tem2, tem3, tem4   
    
    # Characters 
    nessie = Characters("nessie","Nessie.png", 75, 75)
    img = loadImage('Nessie.png')
    moth = Characters("moth","MothMan.png", 75, 75)
    img1 = loadImage('MothMan.png')
    bf = Characters("bf","Big Foot.png", 75, 75)
    img2 = loadImage('Big Foot.png')
    yeti = Characters("yeti","Yeti.png", 75, 75)
    img3 = loadImage('Yeti.png')

    #Items/ Hiding places 
    lamp = Item("lamp", "Lampost.png", 75, 75 )
    tem = loadImage('Lampost.png')
    tank = Item("tank", "WaterTank.png", 75, 75 )
    tem1 = loadImage('WaterTank.png')
    photo = Item("photo", "Photo.png", 75, 75 )
    tem2 = loadImage('Photo.png')
    snow = Item("snow", "Snow.png", 75, 75 )
    tem3 = loadImage('Snow.png')
    cocoa = Item("cocoa", "Cocoa.png", 75, 75 )
    tem4 = loadImage('Cocoa.png')
    
    #locations
    camp = Locs("camp", "Camp.png", 75, 75)
    loc = loadImage('Camp.png')
    forest = Locs("forest", "Forest.png", 75, 75)
    loc1 = loadImage('Forest.png')
    lake = Locs("lake", "Lake.png", 75, 75)
    loc2 = loadImage('Lake.png')
    cave = Locs("cave", "Cave.png", 75, 75)
    loc3 = loadImage('Cave.png')
    road = Locs("road", "Roadside.png", 75, 75)
    loc4 = loadImage('Roadside.png')
    
def draw():
     background(55)
     global Answer1, Answer2, Answer3, NessieReaction1, NessieReaction2, NessieReaction3


    
    #lamp.display(tem)
    #tank.display(tem1)
    #photo.display(tem2)
    #snow.display(tem3)
    #cocoa.display(tem4)
    
    #camp.display(loc)
    #lake.display(loc2)
    #forest.display(loc1)
    #cave.display(loc3)
    #road.display(loc4)
    
    #nessie.display(img)
    #moth.display(img1)
    #bf.display(img2)
    #yeti.display(img3)
    
    #blend(loc,0, 0, 33, 100, 67, 0, 33, 100, LIGHTEST)
    
    
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
    
    #startScreen()
    letter = loadImage("Letter.png")
    image(letter, 0,0) 
        
        
    if (Answer1):
        textSize(28)
        fill(120)
        text("Press 1 for: Answer1", 12, 200)
        
    if (Answer2):
        textSize(28)
        fill(120)
        text("Press 2 for: Answer2", 12, 240)
        
    if (Answer3):
        textSize(28)
        fill(120)
        text("Press 3 for: Answer3", 12, 280)
        
    if (NessieReaction1):
        textSize(28)
        fill(120)
        text("yay! Text option 1", 14, 550)
        
    if (NessieReaction2):
        textSize(28)
        fill(120)
        text("yay! Text option 1", 14, 550)
        
    if (NessieReaction3):
        textSize(28)
        fill(120)
        text("yay! Text option 1", 14, 550)
        
        

def keyPressed():
    global Answer1, Answer2, Answer3, NessieReaction1, NessieReaction2, NessieReaction3
    
                                 #MOTHMAN
if ((key == 'a')):
        Answer1 = True
        Answer2 = True
        Answer3 = True

    
    #answer1
    if ((key == '1')):
        Answer1 = True
        Answer2 = False
        Answer3 = False
        NessieReaction1 = True
    #answer2
    if ((key == '2')):
        Answer2 = True
        Answer1 = False
        Answer3 = False
        NessieReaction1 = True
   #answer3 
    if ((key == '3')):
        Answer3 = True
        Answer2 = False
        Answer1 = False
        NessieReaction1 = True
        
        
    
   
