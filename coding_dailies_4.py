#									~CODING DAILIES~

# 4 - Random weather descriptions

import random

weather_desc = [
    "The weather is clear, and the sun is bright overhead.",
    "A light fog encapsulates the local area. It is slightly hard to see.",
    "It is dark and gloomy, with very little light available.",
    "It is dimly lit, the moon supplying the area with some of its glow."
]

def look_weather_desc():
    random_weather_chosen = random.choice(weather_desc)
    return print(random_weather_chosen)

print("Type 'look weather' to see what the weather is like at this moment.")
user_input = input()

if user_input == ("look weather"):
    look_weather_desc()
else:
    print("That is not a valid command.")