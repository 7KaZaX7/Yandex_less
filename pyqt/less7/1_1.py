import random

with open("*.txt") as file:
    lines = file.readlines()

if not lines:
    print('')
else:
    print(random.choice(lines).strip())
