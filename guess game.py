import random

n = random.randint(1, 100)
while (g := int(input("Guess: "))) != n:
    print("Too low!" if g < n else "Too high!")
print("You got it!")