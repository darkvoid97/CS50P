import sys, os

if error:=("Too few command-line arguments" if len(args:=sys.argv) <= 1 else "Too many command-line arguments" if len(args) > 2 else "Not a Python file" if not args[1].endswith('.py') else "File does not exist" if not os.path.isfile(args[1]) else None):
    sys.exit(error)

with open(args[1], "r") as file:
    print(sum(1 for line in file if (stripped:=line.strip()) and not stripped.startswith("#")))
