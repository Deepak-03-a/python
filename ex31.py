print "You entere a dark room with two door. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a gaint bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input(">")
    
    if bear == "1":
        print "The bear eat your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear rruns away." % bear
 
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Bueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body surrvives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
        
else:
    print "You stumble around and fall on a knife and die. Good job!"
    