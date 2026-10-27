transactions = [
    {"type": "income", "amount": 150},
    {"type": "expense", "amount": 20},
    {"type": "expense", "amount": 15}
]

balance = 0

for item in transactions:
    if item["type"] == "income":
        balance += item["amount"]
    else:
        balance -= item["amount"]

print(f"Balance: {balance} AZN")