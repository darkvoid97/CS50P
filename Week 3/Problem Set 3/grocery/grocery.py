grocery = {}
while True:
    try:
        grocery.update({(item := input().lower()): 1 if item not in grocery else grocery[item]+1})
    except (EOFError):
        break

for i in sorted(grocery):
    print(str(grocery[i]) + " " + str(i).upper())
