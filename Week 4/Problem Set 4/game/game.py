import random

while True:
    if (level := input("Level: ")).isdigit() and int(level) > 0:
        break

choice = random.randint(1, int(level))
while True:
    if (guess := input("Guess: ")).isdigit() and int(guess) > 0:
        print("Too small!" if (int(guess) < choice) else "Too large!" if (int(guess) > choice) else "Just right!")
        if int(guess) == choice:
            break
