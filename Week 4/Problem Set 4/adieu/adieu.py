import inflect

names = []
while True:
    try:
        names.append(input())
    except (EOFError):
        break

print("Adieu, adieu, to " + inflect.engine().join(names))
