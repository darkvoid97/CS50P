def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (len(s) < 2 or len(s) > 6) or (not s[:2].isalpha()) or (not s.isalnum()) or (not check_numbers(s)):
        return False
    return True


def check_numbers(p):
    index = 0
    for c in p:
        if c.isdigit():
            if p[index:].isdigit():
                if c != "0":
                    return True
                return False
            return False
        index += 1
    return True

if __name__ == "__main__":
    main()
