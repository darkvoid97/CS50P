def main():
    tm = convert(input("What time is it?\n"))
    if 7 <= tm <= 8:
        print("breakfast time")
    if 12 <= tm <= 13:
        print("lunch time")
    if 18 <= tm <= 19:
        print("dinner time")


def convert(time):
    tm = time.split()
    hours, minutes = tm[0].split(":")
    if len(tm) == 2:
        hours = "0" if hours == "12" and tm[1] == "a.m." else hours
        hours = float(hours) + (12 if tm[1] == "p.m." and float(hours) != 12 else 0)
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
