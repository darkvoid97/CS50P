def main():
    print("$" + str(value(input("Greeting: "))))


def value(greeting):
    return 0 if (greeting.lstrip().lower()).startswith("hello") else 20 if greeting.lstrip().lower().startswith("h") else 100


if __name__ == "__main__":
    main()
