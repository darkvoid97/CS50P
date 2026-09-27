import requests, sys

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit(1)
try:
    btc = float(sys.argv[1])
    if len(sys.argv) > 2:
        raise ValueError
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
try:
    print(f"${(btc * float(requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=7992298e1f286681cd0f87b4f936f7875f5cd42addc5be2ae1492dd0e712f6af").json()["data"]["priceUsd"])):,.4f}")
except requests.RequestException:
    print("Error with handling the request")
    sys.exit(1)
