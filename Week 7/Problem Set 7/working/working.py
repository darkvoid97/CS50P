import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    matched = re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s)

    if not matched:
        raise ValueError()

    h1, m1, p1, h2, m2, p2 = matched.groups()
    if not (1 <= int(h1) <= 12) or not (1 <= int(h2) <= 12) or (m1 and int(m1) >= 60) or (m2 and int(m2) >= 60):
        raise ValueError()

    def to_24(hour, minutes, am_pm):
        hour = int(hour)
        minutes = minutes if minutes else "00"

        if am_pm == "AM":
            if hour == 12:
                hour = 0
        else:
            if hour != 12:
                hour += 12

        return f"{hour:02d}:{minutes}"

    return f"{to_24(h1, m1, p1)} to {to_24(h2, m2, p2)}"


if __name__ == "__main__":
    main()
