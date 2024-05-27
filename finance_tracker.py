def add_transaction(transactions, type):
    print()
    description = input("Enter a description: ")
    amount = float(input(f"Enter the {type} amount: "))
    transactions.append({"type": type,
                        "description": description,
                         "amount": amount})


def view_summary(transactions):
    total_income = \
        sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expenses = \
        sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = total_income - total_expenses

    print("\nSummary:")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Balance: ${balance}")


def save_data(transactions, filename):
    with open(filename, "w") as file:
        for t in transactions:
            file.write(f"{t['type']},{t['description']},{t['amount']}\n")


def load_data(filename):
    transactions = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                type, description, amount = line.strip().split(",")
                transactions.append(
                    {"type": type,
                     "description": description,
                     "amount": float(amount)})
    except FileNotFoundError:
        print("No previous data found. Starting fresh.")
    return transactions


def main():
    filename = "transactions.txt"
    transactions = load_data(filename)

    while True:
        print()
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Save and Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_transaction(transactions, "income")
        elif choice == "2":
            add_transaction(transactions, "expense")
        elif choice == "3":
            view_summary(transactions)
        elif choice == "4":
            save_data(transactions, filename)
            print("Data saved. Exiting")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
