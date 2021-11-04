#									~CODING DAILIES~

# 8 - making/planning a character statistic layout

from coding_dailies_8_BaseCharacter import BaseCharacter

# test_character_one = BaseCharacter("Player One", 11, 12, 13, 14, 15)
# test_character_one.print_name()
# test_character_one.print_stats()

test_character_two = BaseCharacter("Player Two", 15, 14, 13, 12, 11)
test_character_two.stats_assign_strength()
test_character_two.stats_assign_intelligence()
test_character_two.stats_assign_wisdom()
test_character_two.stats_assign_dexterity()
test_character_two.stats_assign_constitution()
test_character_two.print_stats()