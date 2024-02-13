#!/bin/usr/python3

# define the distance a disc should fly

discs = {"putter": 250, "midrange": 275, "fairway driver": 350, "distance driver": 400}

# ask the user how long the hole is
hole_length = int(input("how long is the hole, bro? (in feet, my man): "))


# check which disc would work based on the input from the user

if hole_length <= discs["putter"]:
    throw_this = "putter"
elif hole_length >= discs["midrange"]-25 and hole_length <= discs["midrange"]+25:
    throw_this = "midrange"
elif hole_length <= discs["fairway driver"]:
    throw_this = "fairway driver"
else:
    throw_this = "distance driver"

# display the suggested disc

print("Man, I am not sure how good you are, but I would say if the hole is", hole_length, "I would throw a", throw_this + ".") 

 
