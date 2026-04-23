import json
import os

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(transactions):
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=2)
def add_transaction(transactions, kind):
    description = input(f"Description of {kind}: ")
    amount = float(input("Amount: "))

    transactions.append({
        "type": kind,
        "description": description,
        "amount": amount
    })

    save_data(transactions)
    print(f"{kind.capitalize()} added!")

def view_balance(transactions):
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expenses
    print(f"\nIncome:   ${income:.2f}")
    print(f"Expenses: ${expenses:.2f}")
    print(f"Balance:  ${balance:.2f}")

def view_transactions(transactions):
    if not transactions:
        print("No transactions yet.")
        return
    for t in transactions:
        sign = "+" if t["type"] == "income" else "-"
        print(f"  {sign} ${t['amount']:.2f}  |  {t['description']}")
def main():
    transactions = load_data()

    while True:
        print("\n--- Budget Tracker ---")
        print("1. Add income")
        print("2. Add expense")
        print("3. View balance")
        print("4. View all transactions")
        print("5. Quit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_transaction(transactions, "income")
        elif choice == "2":
            add_transaction(transactions, "expense")
        elif choice == "3":
            view_balance(transactions)
        elif choice == "4":
            view_transactions(transactions)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

main()