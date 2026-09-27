import sys, os, csv

if error:=("Too few command-line arguments" if len(args:=sys.argv) <= 2 else "Too many command-line arguments" if len(args) > 3 else "Not a CSV file" if not args[1].endswith('.csv') else "File does not exist" if not os.path.isfile(args[1]) else None):
    sys.exit(error)

with open(args[1], "r") as before:
    reader = csv.DictReader(before)
    with open(args[2], "w") as after:
        writer = csv.DictWriter(after, fieldnames=['first','last','house'])
        writer.writeheader()
        for row in reader:
            writer.writerow({'first': (fullname := row['name'].split(', '))[1], 'last':fullname[0], 'house':row['house']})
