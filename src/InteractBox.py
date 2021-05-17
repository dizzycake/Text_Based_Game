class Interact(object):
    
    #NOTE: Checkout how to rewrite this using same logic as strtscreen
    #Use gdshfgdas = "jhgsfjhgds" instead of if statements
    
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

    def __init__(self, name, imageName, x, y):
        self.name = name
        self.imageName = imageName

    def display(self, img):
            global NessieQuestion, NAnswer1, NAnswer2, NAnswer3, NReaction1, NReaction2, NReaction3 

            #NESSIE
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
