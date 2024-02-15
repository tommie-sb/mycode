#!usr/bin/python3
"""This is Tommie's Project to conclude this program"""

#FIRST, IMPORT THE DICIONARY OF DISCS INTO MY CODE
from bag import discs
import crayons

#THIS FUNCTION CLASSIFIES WHAT KIND OF DISC IT IS, BASED ON ITS SPEED
def classify_disc(speed):
    if speed <= 3:
        return (crayons.red("Putter"))
    elif speed <= 5:
        return (crayons.blue("Midrange"))
    elif speed <= 9:
        return (crayons.yellow("Fairway Driver"))
    else:
        return (crayons.magenta("Distance Driver"))

#THIS FUNCTION WILL DISPLAY THE CONTENTS AND ATTRIBUTES OF THE DISCS IMPORTED
def bag_info(huh):
    if huh == "inventory":
        print("Here's what you're working with:")
        for disc_name in discs:
            print("-", disc_name)
    elif huh == "type":
        print("Here's the different types of discs in your bag:")
        for disc_name, disc_info in discs.items():
            speed = disc_info["speed"]
            disc_type = classify_disc(speed)
            print("-", disc_name, "(Type:", disc_type + ")")

        #for disc_name, disc_info in discs.items():
            #print("-", disc_name, "(Type:", classify_disc(disc_info["speed"]))
    else:
        print(f"C'mon man, play by the rules and pick a valid response")

#WHAT DOES THE USER WANT TO DO WITH THEIR BAG?
huh = input("Bro, what do you want to know about your bag? (Inventory, type, or attributes?:)")

bag_info(huh.lower())
