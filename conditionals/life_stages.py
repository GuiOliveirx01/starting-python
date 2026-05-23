age = int(input("How old are you? "))

if age < 2:
    print("You're a baby.")
elif age < 4:
    print("You're a child.")
elif age < 13:
    print("You're a kid.")
elif age < 20:
    print("You're a teenager.")
elif age < 65:
    print("You're a adult.")
else:
    print("You're a elderly.")