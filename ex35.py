from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, lean to type a number.")
    
    if how_much < 50:
        print "Nice, you are not greedy, you win!"
        exit(0)
    else:
        dead("You gready bastard!")


def bear_room():
    print "Ther is a bear here."
    print "The bear has a bunch of honey."
    print "The fat beat is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at yoy then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear moved from the door. you can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."



def cthulhu_room():
    print "Here you see the great evil cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    nexr = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)
    
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which on do you take?"
    
    next = raw_input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumbled around the room until you starve.")
        

start()

    
    
 
            
        
    