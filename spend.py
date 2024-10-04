import matplotlib.pyplot as plt

class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            print("List of expenses:")
            for index, expense in enumerate(self.expenses, start=1):
                print(f"{index}. {expense.name}: ${expense.amount} ({expense.category})")

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def expenses_by_category(self):
        categories = {}
        for expense in self.expenses:
            categories[expense.category] = categories.get(expense.category, 0) + expense.amount
        return categories

    def plot_expenses_by_category(self):
        expenses_by_category = self.expenses_by_category()
        categories = list(expenses_by_category.keys())
        amounts = list(expenses_by_category.values())

        plt.figure(figsize=(10, 6))
        plt.bar(categories, amounts, color='skyblue')
        plt.xlabel('Categories')
        plt.ylabel('Amount ($)')
        plt.title('Expenses by Category')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. View Expenses by Category (Graph)")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            expense = Expense(name, amount, category)
            tracker.add_expense(expense)
            print("Expense added successfully!")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            total = tracker.total_expenses()
            print(f"Total expenses: ${total}")
        elif choice == "4":
            expenses_by_category = tracker.expenses_by_category()
            print("Expenses by Category:")
            for category, amount in expenses_by_category.items():
                print(f"{category}: ${amount}")
        elif choice == "5":
            tracker.plot_expenses_by_category()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
