# create a mapping of state to abbreviation
states = {'Oregon': 'OR', 'Florida' : 'FL', 'California' : 'CA', 'New York' : 'NY', 'Michigan' : 'MI'}

# create a basic set of states and some cities in them
cities = {'CA' : 'San Francisco', 'MI' : 'Detroit', 'FL' : 'Jacksonville'}

# add some more cities
cities['NY'] = 'New york'
cities['OR'] = 'Portland'

# print out some cities
print '_' *10
print "NY state has: ", cities['NY']
print "OR state has :", cities['OR']

# oritn some states 
print '_' *10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbrevation is: ", states['Florida']

# do it by using the state then cities dict
print '_' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbrevation
print '_' * 10
for state, abbrev in states.items():
    print "%s is abbrevated %s" % (state, abbrev)
    
# print every city in state
print '_' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" %(abbrev, city)

# now do both at the same time
print '_' * 10
for state, abbrev in states.items():
    print "%s state is abbrevated %s and has city %s" %(state, abbrev, cities[abbrev])
  
 print '_' * 10 
 # safety get an abbreviation by state that might not be there
 state = states.get('Texas', None)
 
 if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', Does Not Exist')
print "The city for the state 'TX' is : %s" % city
    

    