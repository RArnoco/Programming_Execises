#exercise18_Names, Variables, Codes, Functions !
#this one is like scripts /args

def print_two(*args):
    arg1, arg2 = args
    print (f"arg1:{arg1}, arg2: {arg2}")

#another example, zed said this is pointless..

def print_two_again(arg1, arg2):
    print (f"arg1: {arg1}, arg2: {arg2}")

#ok I get it, same output, different statements/ let's try another one
#this one only takes one argument :3
def print_one (arg1):
    print (f"arg1: {arg1}")

#this one takes no argument, interesting..

def print_none():
    print ("I got nothing")

print_two ("zed", "shaw") #cool name of the author
print_two_again ("Rey", "A") #how about mine
print_one ("Only one print!") #yep this is function print_one
print_none () #none