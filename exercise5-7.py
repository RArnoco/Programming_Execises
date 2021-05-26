# -*- coding: utf-8 -*-
#exercise05_more variables and printing
#variable declarations
my_name = 'Rey'
my_age = 24 #hehehe
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

#print of variables with string
print ("Let's talk about %s." %my_name)
print ("he's %d inches tall." %my_height)
print ("He's actually that's not too heavy.")
print ("He's got %s eyes and %s hair" % (my_eyes, my_hair))
print ("His teeth are usally %s depending on the coffee" % my_teeth)

#combine
print ("If I add %d, %d. and %d and get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

#----------------------------------------------------------------------------

#exercise06_Strings and Text
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print (x)
print (y)

print  ("I said: %r." %x)
print  ("I also said: %r." %y)

hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with the right side."

print  (w+e)

#----------------------------------------------------------------------------
#exericise07_printing!
print ("Mary had a little lamb.")
print ("Its fleece was white as %s." % "snow")
print ("And everywhere that Mary went.")

# repeat dot 10 times
print ("." * 10 )

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#combine end values
# the comma makes SPACE
print (end1 + end2 + end3 + end4 + end5 + end6, end7 + end8 + end9 + end10 + end11 + end12)