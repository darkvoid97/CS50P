print((camel := input("Camel case: "))[0].lower() + ''.join('_' + char.lower() if char.isupper() else char for char in camel[1:]))
