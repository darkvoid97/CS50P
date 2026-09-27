import sys, os, csv, tabulate

if error:=("Too few command-line arguments" if len(args:=sys.argv) <= 1 else "Too many command-line arguments" if len(args) > 2 else "Not a CSV file" if not args[1].endswith('.csv') else "File does not exist" if not os.path.isfile(args[1]) else None):
    sys.exit(error)

with open(args[1], "r") as csvfile:
    reader = csv.DictReader(csvfile)
    print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))
