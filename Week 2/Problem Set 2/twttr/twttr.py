print("Output: " + ''.join(char if char.lower() not in ("a","e","i","o","u") else "" for char in input("Input: ")))
