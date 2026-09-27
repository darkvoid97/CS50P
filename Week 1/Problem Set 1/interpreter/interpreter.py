x,y,z = input("Expression: ").split()
match y:
    case "+":
        print(f"{float(int(x)+int(z)):.1f}")
    case "-":
        print(f"{float(int(x)-int(z)):.1f}")
    case "*":
        print(f"{float(int(x)*int(z)):.1f}")
    case "/":
        if int(z) == 0:
            print("Can not divide by zero.")
        else:
            print(f"{float(int(x)/int(z)):.1f}")
