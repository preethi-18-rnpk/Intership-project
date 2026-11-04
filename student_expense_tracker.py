# Student Expense Tracker

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    print("Expense added successfully!")

def view_expenses():
    total = 0

    print("\nYour Expenses:")

    for expense in expenses:
        print(expense["name"], "-", expense["amount"])
        total += expense["amount"]

    print("Total Expense:", total)

while True:
    print("\n--- Student Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
