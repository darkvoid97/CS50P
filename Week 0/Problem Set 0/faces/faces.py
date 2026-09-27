def convert(text: str):
    return text.replace(":)","🙂").replace(":(","🙁")

def main():
    print(convert(input("Bro gimme smiles and/or frowns :)\n")))

if __name__ == "__main__":
    main()
