#!usr/bin/python3
"""This is Tommie's Project to conclude this program"""

#FIRST, IMPORT THE DICIONARY OF DISCS INTO MY CODE
from bag import discs

print("names:")
for disc_name in discs.items():
    print("-", disc_name["speed"])
