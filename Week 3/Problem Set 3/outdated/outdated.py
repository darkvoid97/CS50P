months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    mm, dd, yyyy = date.split("/") if "/" in (date := input("Date: ").strip()) else date.replace(",","").split() if ", " in date else ["INVALID","INVALID","INVALID"]
    if ((mm.isdigit() and 1 <= int(mm) <= 12 and "," not in date) or (mm.isalpha() and mm in months and "/" not in date)) and (dd.isdigit() and 1 <= int(dd) <= 31):
        print(f"{yyyy}-" + (f"{int(mm):02}" if mm.isdigit() else f"{(months.index(mm)+1):02}") + f"-{int(dd):02}")
        break
