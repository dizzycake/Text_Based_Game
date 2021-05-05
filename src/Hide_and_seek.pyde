# Hide And Seek - Text Based Game
# by Joanna Bromka and Kate Nelson | 2021 Programming I

# TO DO LIST

from Locations import Locations
locations1 = Locations()
from Characters import Characters
nessie = Characters("nessie","Nessie.png" 75, 75)


def setup():
    size(700, 500)


def draw():
    background(0)
    rect(300, 200, 100, 100)
    locations1.display()
    nessie.display()
