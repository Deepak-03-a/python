the_count = [1, 2, 3, 4, 5]
fruits = ['apples' , 'oranges' , 'pears' , 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

#same as above
for fruit in fruits:
    print  ("A fruit of type: {}" .format(fruit))
    
# also we can go through mixed lists too 
# notice we have to use %r since we don't know what's in it
for i in change:
    print ("I gor {}" .format(change))

# we can also build lists, first stat with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print ("Adding {} to the list." .format(i))
    # append is a fucntion that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print ("Element was: {}" .format(i))
    