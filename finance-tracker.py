# Add income and expenses to a list of transactions
def add_transaction(transactions, type):
    print()
    # Get the description and amount of the transaction from the user
    description = input("Enter a description: ")
    # The float() function converts the input to a floating-point number
    amount = float(input(f"Enter the {type} amount: "))
    # Append a dictionary to the transactions list
    transactions.append({"type": type,
                        "description": description,
                         "amount": amount})


# View a summary of the transactions
def view_summary(transactions):
    # Calculate the total income, total expenses, and balance
    # using a list comprehension and the sum() function

    # If the transaction type is 'income', add the amount to the total_income
    total_income = \
        sum(t['amount'] for t in transactions if t['type'] == 'income')

    # If the transaction type is 'expense', add the amount to the total_expenses
    total_expenses = \
        sum(t['amount'] for t in transactions if t['type'] == 'expense')

    # Calculate the balance by subtracting total_expenses from total_income
    balance = total_income - total_expenses

    # Print the summary
    print("\nSummary:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")


# Save data to a file
def save_data(transactions, filename):
    # The open(file, mode) function opens a file, and returns a file object.
    # mode: 'r' for reading, 'w' for writing, 'a' for appending, etc.
    with open(filename, "w") as file:
        # Iterate over the transactions list and write each transaction to the file
        for t in transactions:
            # Write the transaction as a comma-separated string
            file.write(f"{t['type']},{t['description']},{t['amount']}\n")


# Load data from a file
def load_data(filename):
    # Initialize an empty list to store the transactions
    transactions = []
    try:
        # The open(file, mode) function opens a file, and returns a file object.
        # mode: 'r' for reading, 'w' for writing, 'a' for appending, etc.
        with open(filename, 'r') as file:
            for line in file:
                # Split the line into its components and unpack them into variables
                type, description, amount = line.strip().split(",")
                # Append a dictionary to the transactions list
                transactions.append(
                    {"type": type,
                     "description": description,
                     "amount": float(amount)})
    # If the file is not found, catch the FileNotFoundError exception
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
            print(transactions)
            break
        else:
            print("Invalid choice. Please try again.")


# The __name__ variable contains the name of the module that is being run.
# If the module is being run as the main program, the __name__ variable will be set to "__main__".
# In this case, we call the main() function to start the program.
if __name__ == "__main__":
    main()
