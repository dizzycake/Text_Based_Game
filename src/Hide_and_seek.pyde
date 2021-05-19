#Hide And Seek - Text Based Game
# by Joanna Bromka and Kate Nelson | 2021 Programming I

# TO DO LIST

#Needed fpr keypressed
NessieQuestion = False
    MothmanQuestion = False
    BigfootQuestion = False
    YetiQuestion = False

    NAnswer1 = False
    NAnswer2 = False
    NAnswer3 = False

    MAnswer1 = False
    MAnswer2 = False
    MAnswer3 = False

    BAnswer1 = False
    BAnswer2 = False
    BAnswer3 = False

    YAnswer1 = False
    YAnswer2 = False
    YAnswer3 = False

    NReaction1 = False
    NReaction2 = False
    NReaction3 = False

    MReaction1 = False
    MReaction2 = False
    MReaction3 = False
    
    BReaction1 = False
    BReaction2 = False
    BReaction3 = False

    YReaction1 = False
    YReaction2 = False
    YReaction3 = False

#from Locations import Locations
from Characters import Characters
from Locations import Locs
from Items import Item

        
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
    nessie.display(img)
    global NessieQuestion, NAnswer1, NAnswer2, NAnswer3, NReaction1, NReaction2, NReaction3 
   
    if (play == False):
        startScreen()
    else:
    
  
    # chatBox
    strokeWeight(7)
    stroke(235, 237, 236)
    fill(0)
    rect(0, 480, 900, 220)

    # interact box
    strokeWeight(7)
    stroke(235, 237, 236)
    fill(0)
    rect(0, 0, 300, 480)
            
    if (NessieQuestion):
        textSize(32)
        fill(120)
        text("Question1", 80, 90)
        textSize(28)
        text("Press a for answers", 23, 150)
        
    if (NAnswer1):
        textSize(28)
        fill(120)
        text("Press 1 for: Answer1", 12, 200)
        
    if (NAnswer2):
        textSize(28)
        fill(120)
        text("Press 2 for: Answer2", 12, 240)
        
    if (NAnswer3):
        textSize(28)
        fill(120)
        text("Press 3 for: Answer3", 12, 280)
        
    if (NReaction1):
        textSize(28)
        fill(120)
        text("yay! Text option 1", 14, 550)
        
    if (NReaction2):
        textSize(28)
        fill(120)
        text("yay! Text option 1", 14, 550)
        
    if (NReaction3):
        textSize(28)
        fill(120)
        text("yay! Text option 1", 14, 550)

    
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
    
  
    
    def startScreen()
        letter = loadImage("Letter.png")
        image(letter, 0,0)
        fill(235, 237, 236)
        text("Dear Jack, ", 10, 300)
        start = "We have invited you to join the Cryptid Book Club! Meet all the other members at the Curious Campgrounds to join us, and make sure to bring some good books!";
        text(start, 20, 315, 280, 400)
        instruct= "- Sincerly, CBC Cryptids"
        text(instruct, 20, 390, 280, 420)
        instruct= "Use the 1, 2, & 3 keys to ineract and the arrow keys to switch locations. Click the right arrow to begin"
        text(instruct, 20, 420, 280, 420)
        
 
        
def keyPressed():
    global NessieQuestion, NAnswer1, NAnswer2, NAnswer3, NReaction1, NReaction2, NReaction3 
    
# NESSIE

    if ((key == 'q')):
        NessieQuestion = True
        
    if ((key == 'a')):
        NAnswer1 = True
        NAnswer2 = True
        NAnswer3 = True

    # answer1
    if ((key == '1')):
        NAnswer1 = True
        NAnswer2 = False
        NAnswer3 = False
        NReaction1 = True
    # answer2
    if ((key == '2')):
        NAnswer2 = True
        NAnswer1 = False
        NAnswer3 = False
        NReaction1 = True
   # answer3 
    if ((key == '3')):
        NAnswer3 = True
        NAnswer2 = False
        NAnswer1 = False
        NReaction1 = True
        
        
    
   
