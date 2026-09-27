amount_due: int = 50
while True:
    print(f"Amount due: {amount_due}")
    amount_due -= coin if (coin := int(input("Insert coin: "))) in (25, 10, 5) else 0
    if amount_due <= 0:
        print(f"Change owed: {-amount_due}")
        break
