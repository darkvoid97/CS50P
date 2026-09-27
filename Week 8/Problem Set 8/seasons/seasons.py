import sys, inflect
from datetime import date


def main():
    print(get_date(input("Date of Birth: ")))

def get_date(s):
    try:
        birth_date = date.fromisoformat(s)
    except (ValueError):
        sys.exit("Invalid date")
    return f"{(infl := inflect.engine()).number_to_words(minutes := (int((date.today() - birth_date).days) * 1440), andword='').capitalize()} {infl.plural_noun("minute", minutes)}"

if __name__ == "__main__":
    main()
