#									~CODING DAILIES~

# 3 - Working with input and functions

def load_room():
    return print("You have entered a room.")

print("Hello World!")

print("""You are in a clearing. There are exits to the NORTH, SOUTH, EAST, and WEST.
Type one of these directions to go through that exit.""")

direction_entered = input("Where will you go: ")

if direction_entered.lower() == "north" or direction_entered == "south" or direction_entered == "east" or direction_entered == "west":
    print("You travel " + direction_entered.lower() + ".")
    load_room()
else:
    print("That is not a valid direction.")


