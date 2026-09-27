import random


def main():
    eqn = 10
    score = 0
    chances = 3
    lvl = get_level()
    while eqn != 0:
        if chances == 3:
            x = generate_integer(lvl)
            y = generate_integer(lvl)
        try:
            user_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if user_answer == answer:
                eqn = eqn - 1
                score = score + 1
                chances = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances = chances - 1
            pass
        if chances == 0:
            print((f"{x} + {y} = {answer}"))
            chances = 3
            eqn = eqn - 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass


def generate_integer(level):
    if level == 1:
        r = random.randint(0, 9)
    elif level == 2:
        r = random.randint(10, 99)
    elif level == 3:
        r = random.randint(100, 999)
    return r


if __name__ == "__main__":
    main()
