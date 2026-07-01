def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        with open("expenses.txt", "a") as f:
            f.write(f"{amount},{category}\n")

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount! Please enter a number.")


def view_expenses():
    total = 0

    try:
        with open("expenses.txt", "r") as f:
            lines = f.readlines()

            if not lines:
                print("No expenses recorded.")
                return

            print("\n--- Expense List ---")
            for line in lines:
                amount, category = line.strip().split(",")
                print(f"₹{amount} - {category}")
                total += float(amount)

            print("---------------------")
            print("Total Expense: ₹", total)

    except FileNotFoundError:
        print("No data found. Please add expenses first.")


# Main Program
while True:
    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
