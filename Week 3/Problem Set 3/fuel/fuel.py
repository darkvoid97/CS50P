while True:
    try:
        x, y = input("Fraction: ").split("/")
        if not x.isdigit() or not y.isdigit() or int(x) > int(y):
            raise ValueError
        print((str(tank) + "%") if (1 < (tank := round(int(x)/int(y)*100)) < 99) else "E" if (tank <= 1) else "F")
        break
    except (ValueError, ZeroDivisionError):
        continue
