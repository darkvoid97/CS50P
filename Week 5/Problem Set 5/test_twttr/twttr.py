def main():
    print("Output: " + shorten(input("Input: ")))


def shorten(word):
    return ''.join(char if char.lower() not in ("a","e","i","o","u") else "" for char in word)


if __name__ == "__main__":
    main()
