income = []
expenses = []


def add_income():
    amount = float(input("\nEnter income amount: "))
    income.append(amount)


def add_expense():
    category = input("\nEnter expense category: ")
    amount = float(input("Enter expense amount: "))
    expenses.append({"category": category, "amount": amount})


def calculate_budget():
    total_income = sum(income)
    total_expenses = sum(expense["amount"] for expense in expenses)
    print(f"\nRemaining budget: {total_income - total_expenses}")


def analyze_expenses():
    expense_summary = {}
    for expense in expenses:
        if expense["category"] not in expense_summary:
            expense_summary[expense["category"]] = 0
        expense_summary[expense["category"]] += expense["amount"]
    print("\nExpense Analysis:")
    for category, amount in expense_summary.items():
        print(f"{category}: {amount}")


def main():
    while True:
        print("\n1. Add income")
        print("2. Add expense")
        print("3. Calculate budget")
        print("4. Analyze expenses")
        print("5. Exit")
        choice = input("\nEnter choice: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            calculate_budget()
        elif choice == "4":
            analyze_expenses()
        elif choice == "5":
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
