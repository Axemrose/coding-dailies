# BaseCharacter class for preliminary planning of character stats in AlchemMUD

class BaseCharacter:
    def __init__(self, name, strength, intelligence, wisdom, dexterity, constitution):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.dexterity = dexterity
        self.constitution = constitution

    def print_name(self):
        print("Name: " + str(self.name))

    def print_stats(self):
        print("Strength: " + str(self.strength))
        print("Intelligence: " + str(self.intelligence))
        print("Wisdom: " + str(self.wisdom))
        print("Dexterity: " + str(self.dexterity))
        print("Constitution: " + str(self.constitution))

    def stats_assign_strength(self):
        player_input = input("What number do you want this Character's strength to be: ")
        self.strength = int(player_input)

    def stats_assign_intelligence(self):
        player_input = input("What number do you want this Character's intelligence to be: ")
        self.intelligence = int(player_input)

    def stats_assign_wisdom(self):
        player_input = input("What number do you want this Character's wisdom to be: ")
        self.wisdom = int(player_input)

    def stats_assign_dexterity(self):
        player_input = input("What number do you want this Character's dexterity to be: ")
        self.dexterity = int(player_input)

    def stats_assign_constitution(self):
        player_input = input("What number do you want this Character's constitution to be: ")
        self.constitution = int(player_input)
