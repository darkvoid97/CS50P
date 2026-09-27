def main():
    try:
        print(gauge(convert(input("Fraction: "))))
    except (ValueError, ZeroDivisionError):
        return


def convert(fraction):
    x, y = fraction.split("/")
    if int(y) == 0:
        raise ZeroDivisionError
    if not x.isdigit() or not y.isdigit() or int(x) > int(y):
        raise ValueError
    return round(int(x)/int(y)*100)


def gauge(percentage):
    return (str(percentage) + "%") if (1 < percentage < 99) else "E" if (percentage <= 1) else "F"


if __name__ == "__main__":
    main()
