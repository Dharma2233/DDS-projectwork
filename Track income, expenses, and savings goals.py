import json

class Transaction:
    def __init__(self, t_type, amount, description, month):
        self.t_type = t_type
        self.amount = amount
        self.description = description
        self.month = month

transactions = []

def add_transaction(t_type, amount, description, month):
    transactions.append(Transaction(t_type, amount, description, month))

def save_data(filename):
    with open(filename, "w") as f:
        json.dump([t.__dict__ for t in transactions], f)

def load_data(filename):
    global transactions
    with open(filename, "r") as f:
        data = json.load(f)
        transactions = [Transaction(**d) for d in data]

def sort_transactions():
    return sorted(transactions, key=lambda x: x.amount)

def search_transactions(keyword):
    return [t for t in transactions if keyword.lower() in t.description.lower()]

def filter_expenses(limit):
    return [t for t in transactions if t.t_type == "expense" and t.amount > limit]

def monthly_spending_chart():
    monthly = {}
    for t in transactions:
        if t.t_type == "expense":
            monthly[t.month] = monthly.get(t.month, 0) + t.amount
    for month, total in monthly.items():
        print(f"{month}: {'#' * (total // 10)} {total}")

add_transaction("income", 2000, "salary", "January")
add_transaction("expense", 150, "groceries", "January")
add_transaction("expense", 80, "transport", "January")
add_transaction("expense", 300, "shopping", "February")
save_data("data.json")
load_data("data.json")
for t in sort_transactions():
    print(t.t_type, t.amount, t.description, t.month)
print("Filtered:", [(t.amount, t.description) for t in filter_expenses(100)])
monthly_spending_chart()
