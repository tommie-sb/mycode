#!usr/bin/python3
"""This is Tommie's Project to conclude this program"""

#FIRST, IMPORT THE DICIONARY OF DISCS INTO MY CODE
from bag import discs
#HAVE FUN WITH CRAYONS AND ENHANCE THE USERS EXPERIENCE
import crayons

#DO SOMETHING FUN WITH MATPLOTLIB?!!!!

#THIS FUNCTION CLASSIFIES WHAT KIND OF DISC IT IS, BASED ON ITS SPEED
def classify_disc(speed):
    if speed <= 3:
        return (crayons.cyan("Putter"))
    elif speed <= 5:
        return (crayons.blue("Midrange"))
    elif speed <= 9:
        return (crayons.yellow("Fairway Driver"))
    else:
        return (crayons.magenta("Distance Driver"))

#THIS FUNCTION WILL DISPLAY THE CONTENTS AND ATTRIBUTES OF THE DISCS IMPORTED
def bag_info():
    while True:
        huh = input("Bro! What would you like to know about your bag? Here are the options... Inventory, Type, Attributes, or just type exit to quit my man: ").lower()
        if huh == "inventory":
            print("Here's what you're working with:")
            for disc_name in discs:
                print("-", disc_name)
        elif huh == "type":
            print("Here's the different types of discs in your bag:")
            for disc_name, disc_info in discs.items():
                speed = disc_info["speed"]
                disc_type = classify_disc(speed)
                print("-", disc_name, disc_type)
        elif huh == "attributes":
            print("Attributes of discs in your bag:")
            for disc_name, disc_info in discs.items():
                print("-", disc_name, ("Speed:", disc_info["speed"], ", Glide:", disc_info["glide"], ", Turn:", disc_info["turn"], ", Fade:", disc_info["fade"], ))
        elif huh == "exit":
            print("Have a great round, bro!")
            break
        else:
            print(crayons.red(f"C'mon man, play by the rules and pick a valid response"))

#THIS IS THE MAIN FUNCTION THAT WILL HELP THE USER DECIDE WHICH DISC TO THROW BASED ON THE INPUT ABOUT THE HOLE

#hole_length = float(input(crayons.green("Aright dude! Let's throw some discs! How long is this one? (only the number in feet): ")))
#dogleg_direction = input(crayons.green("Is it a dogleg left, right? Left, Right, or Nope!: "))


def main(hole_length, dogleg_direction):

    if hole_length <= 200:
        suggested_discs = ["Penrose", "Praxis", "Harp"]
    elif hole_length <= 300:
        suggested_discs = ["Pathfinder", "Trust"]
    elif hole_length <= 400:
        suggested_discs = ["Votum", "Mantra", "Felon"]
    else:
        suggested_discs = ["Grace", "Rive"]

    if dogleg_direction == "left":
        suggested_discs = [disc for disc in suggested_discs if discs[disc]["turn"] <= 0]
    elif dogleg_direction == "right":
        suggested_discs = [disc for disc in suggested_discs if discs[disc]["fade"] >= 3]

    # Display the suggested disc types
    print(f"For a hole length of {hole_length} feet and a dogleg direction of {dogleg_direction}, I would suggest throwing:")
    for disc_name in suggested_discs:
        disc_type = classify_disc(discs[disc_name]["speed"])
        print(f"- {crayons.green(disc_name)} ({disc_type})")



bag_info()

hole_length = int(input(crayons.green("Aright dude! Let's throw some discs! How long is this one? (only the number in feet): ")))
dogleg_direction = input(crayons.green("Is it a dogleg left, right? Left, Right, or Nope!: "))

print(crayons.red("Calculating...."))
main(hole_length, dogleg_direction.lower())
