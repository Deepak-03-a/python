x = "There are %d types of people." %10# Including an integer in a string 
binary = "binary"# creating a variable 
do_not = "don't"# creating another variable 
y = "Those who know %s and those who %s." %(binary, do_not)#we are just calling the variables in a string 

print x # askign it  to show the string which we already created 
print y # askign it  to show the string which we already created 

print "I said: %s." %x #repeating the string inside the string 
print "I also said: '%s'. "%y #repeating the string inside the string

hilarious = False # creating a variable
joke_evaluation = "Isn't that joke so funny?! %r" #repeating the string inside the string
print joke_evaluation % hilarious #repeating the string inside the string

w = "This is the left side of...." # creating a variable
e = "a string with a right side." # creating a variable

print w + e  # making a string inside a string