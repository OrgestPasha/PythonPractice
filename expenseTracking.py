expenses = []


def add_expense(amount: float, category: str, description: str):
    if not amount > 0:
        raise ValueError("Amount need's to be higher than 0")
    expense = {"amount": amount, "category": category, "description": description}
    expenses.append(expense)
    return expense


def calculate_total_expenses():
    return sum(expense["amount"] for expense in expenses)


def calculate_total_by_category(category: str):
    return sum(
        expense["amount"] for expense in expenses if expense["category"] == category
    )


def show_expenses():
    for expense in expenses:
        print(f"""
The amount is {expense["amount"]}
The category is {expense["category"]}
The description is {expense["description"]}
        """)


def populate_dummy_expenses():
    add_expense(12.5, "Food", "Lunch at cafe")
    add_expense(45.0, "Transport", "Monthly subway pass")
    add_expense(7.99, "Food", "Coffee and snack")
    add_expense(120.0, "Shopping", "New shoes")
    add_expense(15.0, "Entertainment", "Movie ticket")
    add_expense(60.0, "Food", "Dinner at restaurant")
    add_expense(30.0, "Transport", "Taxi ride")


populate_dummy_expenses()
show_expenses()

print(f"Total expenses: {calculate_total_expenses()}")
print(f"Total spent on Food: {calculate_total_by_category('Food')}")
print(f"Total spent on Transport: {calculate_total_by_category('Transport')}")
