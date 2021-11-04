#									~CODING DAILIES~

# 5 - using a list of the six ingame Elements, and showing it used with a crude version of the Elemental Sigil spell

element_list = ["Water", "Earth", "Fire", "Air", "Light", "Dark"]

name_input = input("What is your name: ")

def spell_elemental_sigil():
    choose_spell = input("""What type of Elemental Sigil would you like to cast?
[Water, Earth, Fire, Air, Light, or Dark]
""")

    if choose_spell in element_list:
        print("A floating, magical sigil appears before " + name_input + ". It symbolizes the " + choose_spell + " Element.")
    else:
        print("That is not a valid element, try again.")
        spell_elemental_sigil()

spell_elemental_sigil()