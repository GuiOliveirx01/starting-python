import random

alien_color = random.choice(['green', 'yellow', 'red'])

if alien_color == 'green':
    print("Green alien hit: +5 points!")
elif alien_color == 'yellow':
    print("Yellow alien hit: +10 points!")
else:
    print("Red alien hit: +15 points!")