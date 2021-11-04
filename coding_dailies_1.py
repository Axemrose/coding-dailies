#									~CODING DAILIES~

# 1 - Mini Soda Machine (using return statement and string variables)
color_sprite = "transparent"
color_orange_soda = "orange"
color_root_beer = "brown"
color_mountain_dew = "green"

def soda_machine(soda_name):
	if soda_name == "Sprite":
		color_of_soda = color_sprite
	elif soda_name == "Orange Soda":
		color_of_soda = color_orange_soda
	elif soda_name == "Root Beer":
		color_of_soda = color_root_beer
	elif soda_name == "Mountain Dew":
		color_of_soda = color_mountain_dew
	else:
		color_of_soda = "non-existent! Your soda disappears into the aether"

	result = "Your chosen soda rolls out of the vending machine.\nYou notice that its color is " + color_of_soda + "."
	return result

soda_input = input("Which soda do you want: ")
print(soda_machine(soda_input))
# first_try = soda_machine("Sprite")
# print(first_try)