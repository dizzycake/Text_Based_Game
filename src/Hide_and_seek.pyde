# Hide And Seek - Text Based Game
# by Joanna Bromka and Kate Nelson | 2021 Programming I


# from Locations import Locations
from Characters import Characters
from Items import Item
from Locations import Locs


def setup():
    size(900, 700)
    global img, img1, img2, img3, nessie, moth, bf, yeti, camp, forest, lake, cave, road, loc, loc1, loc2, loc3, loc4
    global lamp, tank, photo, snow, cocoa, tem, tem1, tem2, tem3, tem4, letter, play
    
    # Characters
    nessie = Characters("nessie", "Nessie.png", 75, 75)
    img = loadImage('Nessie.png')
    moth = Characters("moth", "MothMan.png", 75, 75)
    img1 = loadImage('MothMan.png')
    bf = Characters("bf", "Big Foot.png", 75, 75)
    img2 = loadImage('Big Foot.png')
    yeti = Characters("yeti", "Yeti.png", 75, 75)
    img3 = loadImage('Yeti.png')

    # Items/ Hiding places
    lamp = Item("lamp", "Lampost.png", 75, 75)
    tem = loadImage('Lampost.png')
    tank = Item("tank", "WaterTank.png", 75, 75)
    tem1 = loadImage('WaterTank.png')
    photo = Item("photo", "Photo.png", 75, 75)
    tem2 = loadImage('Photo.png')
    snow = Item("snow", "Snow.png", 75, 75)
    tem3 = loadImage('Snow.png')
    cocoa = Item("cocoa", "Cocoa.png", 75, 75)
    tem4 = loadImage('Cocoa.png')
    
    # locations
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
    
    play = False
    
def draw():
    background(55)
    global Answer1, Answer2, Answer3, NessieReaction1, NessieReaction2, NessieReaction3, play
    text("Click S to begin . . . ", 200, 500)

    def startScreen():
            play == False
            # InteractBox 
            strokeWeight(7)
            stroke(235, 237, 236)
            fill(0)
            rect(0,0,300,480)

            letter = loadImage("Letter.png")
            image(letter, 0, 0)
            fill(235, 237, 236)
            text("Dear Jack, ", 10, 300)
            start = "We have invited you to join the Cryptid Book Club! Meet all the other members at the Curious Campgrounds to join us, and make sure to bring some good books!";
            text(start, 20, 315, 280, 400)
            instruct = "- Sincerly, CBC Cryptids"
            text(instruct, 20, 390, 280, 420)
            instruct = "Use the 1, 2, & 3 keys to ineract and C, L, F, V keys to switch locations. Click C to begin"
            text(instruct, 20, 420, 280, 420)
            
            # chatBox 
            strokeWeight(7)
            stroke(235, 237, 236)
            fill(0)
            rect(0, 480, 920, 240 )
            
    def boxes():
        # InteractBox 
            strokeWeight(7)
            stroke(235, 237, 236)
            fill(0)
            rect(0,0,320,480)
        # chatBox 
            strokeWeight(7)
            stroke(235, 237, 236)
            fill(0)
            rect(0, 480, 930, 240 )



    
    if ((key == 's')):
        play = False
        startScreen()
        play = True
        
    if ((key == 'c')):
        boxes()
        camp.display(loc)
        fill(235, 237, 236)
        text("Hmm, nothing seems to be here, lets try somewhere else ...", 20, 530)
        
    if ((key == 'v')):
        boxes()
        cave.display(loc3)
        fill(235, 237, 236)
        bf.display(img2)
        blend(loc,0, 0, 33, 100, 67, 0, 33, 100, LIGHTEST)
        
    if ((key == 'f')):
        boxes()
        forest.display(loc1)
        moth.display(img1)
        blend(loc,0, 0, 33, 100, 67, 0, 33, 100, LIGHTEST)
        
    if ((key == 'l')):
        boxes()
        lake.display(loc2)
        nessie.display(img)
        blend(loc,0, 0, 33, 100, 67, 0, 33, 100, LIGHTEST)
        fill(235, 237, 236)
        textSize(14)
        text("""
             Key 1: Hi!
             Key 2: Do you know about the bookclub here?
             Key 3: What are you reading?
             
             """, 10, 500)
        while ((key == 'l')): 
           
            if((key == '1')):
                boxes()
                lake.display(loc2)
                nessie.display(img)
                blend(loc,0, 0, 33, 100, 67, 0, 33, 100, LIGHTEST)
                textSize(14)
                fill(235, 237, 236)
                text(""" Hello Jackie-Jackalope, what brings you 
                to my pond?""", 10, 120)
    
         
