import csv
import os
from datetime import date, datetime

from reports import (
    calculate_average,
    get_highest_expense,
    get_top_category,
    get_category_totals,
    get_monthly_total,
    show_dashboard
)

from charts import (
    show_category_chart,
    show_monthly_chart,
    show_category_pie_chart
)


FILE_NAME = "expenses.csv"
BUDGET_FILE = "budget.txt"


# ==========================================
# LOAD EXPENSES
# ==========================================

def load_expenses():

    expenses = []

    if not os.path.exists(FILE_NAME):
        return expenses

    with open(
        FILE_NAME,
        "r",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            return expenses

        for row in reader:

            if "date" not in row:

                expense = {
                    "date": "Unknown",
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "description": row["description"]
                }

                expenses.append(expense)

            else:

                row["amount"] = float(
                    row["amount"]
                )

                if not row["date"]:
                    row["date"] = "Unknown"

                expenses.append(row)

    return expenses


# ==========================================
# SAVE EXPENSES
# ==========================================

def save_all_expenses(expenses):

    with open(
        FILE_NAME,
        "w",
        newline=""
    ) as file:

        fieldnames = [
            "date",
            "amount",
            "category",
            "description"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for expense in expenses:

            writer.writerow(expense)


# ==========================================
# LOAD BUDGET
# ==========================================

def load_budget():

    if os.path.exists(BUDGET_FILE):

        with open(
            BUDGET_FILE,
            "r"
        ) as file:

            return float(file.read())

    return 0


# ==========================================
# SAVE BUDGET
# ==========================================

def save_budget(budget):

    with open(
        BUDGET_FILE,
        "w"
    ) as file:

        file.write(str(budget))


# ==========================================
# ADD EXPENSE
# ==========================================

def add_expense(expenses):

    print("\n===== ADD EXPENSE =====")

    try:

        amount = float(
            input("Enter amount: ₹")
        )

        if amount <= 0:

            print(
                "Amount must be greater than zero."
            )

            return

    except ValueError:

        print(
            "Please enter a valid number."
        )

        return

    category = input(
        "Enter category: "
    ).strip()

    description = input(
        "Enter description: "
    ).strip()

    if category == "":

        print(
            "Category cannot be empty."
        )

        return

    if description == "":

        print(
            "Description cannot be empty."
        )

        return

    expense = {

        "date": date.today().strftime(
            "%Y-%m-%d"
        ),

        "amount": amount,

        "category": category,

        "description": description
    }

    expenses.append(expense)

    save_all_expenses(expenses)

    print(
        "\nExpense added successfully! ✅"
    )


# ==========================================
# VIEW EXPENSES
# ==========================================

def view_expenses(expenses):

    print("\n===== ALL EXPENSES =====")

    if len(expenses) == 0:

        print(
            "No expenses recorded yet."
        )

        return

    for i, expense in enumerate(
        expenses,
        start=1
    ):

        print(
            f"{i}. "
            f"{expense['date']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )


# ==========================================
# EDIT EXPENSE
# ==========================================

def edit_expense(expenses):

    print("\n===== EDIT EXPENSE =====")

    if len(expenses) == 0:

        print(
            "No expenses available."
        )

        return

    view_expenses(expenses)

    try:

        number = int(
            input(
                "\nEnter expense number to edit: "
            )
        )

        index = number - 1

        if index < 0 or index >= len(expenses):

            print(
                "Invalid expense number."
            )

            return

    except ValueError:

        print(
            "Please enter a valid number."
        )

        return

    expense = expenses[index]

    new_amount = input(
        f"Amount [{expense['amount']}]: ₹"
    ).strip()

    new_category = input(
        f"Category [{expense['category']}]: "
    ).strip()

    new_description = input(
        f"Description [{expense['description']}]: "
    ).strip()

    if new_amount != "":

        try:

            new_amount = float(
                new_amount
            )

            if new_amount <= 0:

                print(
                    "Amount must be greater than zero."
                )

                return

            expense["amount"] = new_amount

        except ValueError:

            print(
                "Invalid amount."
            )

            return

    if new_category != "":
        expense["category"] = new_category

    if new_description != "":
        expense["description"] = new_description

    save_all_expenses(expenses)

    print(
        "Expense updated successfully! ✅"
    )


# ==========================================
# DELETE EXPENSE
# ==========================================

def delete_expense(expenses):

    print("\n===== DELETE EXPENSE =====")

    if len(expenses) == 0:

        print(
            "No expenses available."
        )

        return

    view_expenses(expenses)

    try:

        number = int(
            input(
                "\nEnter expense number to delete: "
            )
        )

        index = number - 1

        if index < 0 or index >= len(expenses):

            print(
                "Invalid expense number."
            )

            return

    except ValueError:

        print(
            "Please enter a valid number."
        )

        return

    confirmation = input(
        "Are you sure? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":

        expenses.pop(index)

        save_all_expenses(expenses)

        print(
            "Expense deleted successfully! 🗑️"
        )

    else:

        print(
            "Delete cancelled."
        )


# ==========================================
# SEARCH EXPENSE
# ==========================================

def search_expense(expenses):

    print("\n===== SEARCH EXPENSE =====")

    keyword = input(
        "Enter category or description: "
    ).strip().lower()

    if keyword == "":
        print("Search cannot be empty.")
        return

    found = False

    for i, expense in enumerate(
        expenses,
        start=1
    ):

        category = expense[
            "category"
        ].lower()

        description = expense[
            "description"
        ].lower()

        if (
            keyword in category
            or keyword in description
        ):

            found = True

            print(
                f"{i}. "
                f"{expense['date']} | "
                f"₹{expense['amount']:.2f} | "
                f"{expense['category']} | "
                f"{expense['description']}"
            )

    if not found:

        print(
            "No matching expenses found."
        )


# ==========================================
# TOTAL
# ==========================================

def calculate_total(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(
        f"\nTotal spending: ₹{total:.2f}"
    )


# ==========================================
# CATEGORY SUMMARY
# ==========================================

def category_summary(expenses):

    print("\n===== CATEGORY SUMMARY =====")

    categories = get_category_totals(
        expenses
    )

    if len(categories) == 0:

        print(
            "No expenses available."
        )

        return

    for category, total in categories.items():

        print(
            f"{category}: ₹{total:.2f}"
        )


# ==========================================
# HIGHEST EXPENSE
# ==========================================

def highest_expense(expenses):

    highest = get_highest_expense(
        expenses
    )

    if highest is None:

        print(
            "No expenses available."
        )

        return

    print("\n===== HIGHEST EXPENSE =====")

    print(
        f"Date: {highest['date']}"
    )

    print(
        f"Amount: ₹{highest['amount']:.2f}"
    )

    print(
        f"Category: {highest['category']}"
    )

    print(
        f"Description: {highest['description']}"
    )


# ==========================================
# SET BUDGET
# ==========================================

def set_monthly_budget():

    print("\n===== SET MONTHLY BUDGET =====")

    try:

        budget = float(
            input(
                "Enter monthly budget: ₹"
            )
        )

        if budget <= 0:

            print(
                "Budget must be greater than zero."
            )

            return

        save_budget(budget)

        print(
            "Budget saved successfully! ✅"
        )

    except ValueError:

        print(
            "Please enter a valid number."
        )


# ==========================================
# BUDGET STATUS
# ==========================================

def budget_status(expenses, budget):

    current_month = date.today().strftime(
        "%Y-%m"
    )

    monthly_total = get_monthly_total(
        expenses,
        current_month
    )

    if budget == 0:

        print(
            "No monthly budget has been set."
        )

        return

    remaining = budget - monthly_total

    percentage = (
        monthly_total / budget
    ) * 100

    print(
        "\n===== BUDGET STATUS ====="
    )

    print(
        f"Budget: ₹{budget:.2f}"
    )

    print(
        f"Spent: ₹{monthly_total:.2f}"
    )

    print(
        f"Remaining: ₹{remaining:.2f}"
    )

    print(
        f"Used: {percentage:.2f}%"
    )


# ==========================================
# MONTHLY SUMMARY
# ==========================================

def monthly_summary(expenses):

    print("\n===== MONTHLY SUMMARY =====")

    months = {}

    for expense in expenses:

        if expense["date"] == "Unknown":
            continue

        month = expense["date"][:7]

        if month in months:
            months[month] += expense["amount"]
        else:
            months[month] = expense["amount"]

    for month, total in sorted(
        months.items()
    ):

        print(
            f"{month}: ₹{total:.2f}"
        )


# ==========================================
# VIEW MONTH
# ==========================================

def view_month_expenses(expenses):

    month = input(
        "Enter month (YYYY-MM): "
    ).strip()

    try:

        datetime.strptime(
            month,
            "%Y-%m"
        )

    except ValueError:

        print(
            "Invalid month format."
        )

        return

    found = False
    total = 0

    print(
        f"\n===== EXPENSES FOR {month} ====="
    )

    for expense in expenses:

        if expense["date"].startswith(month):

            found = True

            total += expense["amount"]

            print(
                f"{expense['date']} | "
                f"₹{expense['amount']:.2f} | "
                f"{expense['category']} | "
                f"{expense['description']}"
            )

    if not found:

        print(
            "No expenses found."
        )

    else:

        print(
            f"\nTotal: ₹{total:.2f}"
        )


# ==========================================
# MAIN MENU
# ==========================================

def main():

    expenses = load_expenses()

    budget = load_budget()

    while True:

        print("\n")
        print("=" * 45)
        print("       SMART EXPENSE TRACKER V8")
        print("=" * 45)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Search Expense")
        print("6. Calculate Total")
        print("7. Category Summary")
        print("8. Highest Expense")
        print("9. Set Monthly Budget")
        print("10. Budget Status")
        print("11. Show Category Chart")
        print("12. Monthly Summary")
        print("13. View Month Expenses")
        print("14. Monthly Spending Chart")
        print("15. Category Pie Chart")
        print("16. Dashboard")
        print("17. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            add_expense(expenses)

        elif choice == "2":

            view_expenses(expenses)

        elif choice == "3":

            edit_expense(expenses)

        elif choice == "4":

            delete_expense(expenses)

        elif choice == "5":

            search_expense(expenses)

        elif choice == "6":

            calculate_total(expenses)

        elif choice == "7":

            category_summary(expenses)

        elif choice == "8":

            highest_expense(expenses)

        elif choice == "9":

            set_monthly_budget()

            budget = load_budget()

        elif choice == "10":

            budget_status(
                expenses,
                budget
            )

        elif choice == "11":

            show_category_chart(
                expenses
            )

        elif choice == "12":

            monthly_summary(
                expenses
            )

        elif choice == "13":

            view_month_expenses(
                expenses
            )

        elif choice == "14":

            show_monthly_chart(
                expenses
            )

        elif choice == "15":

            show_category_pie_chart(
                expenses
            )

        elif choice == "16":

            current_month = date.today().strftime(
                "%Y-%m"
            )

            show_dashboard(
                expenses,
                budget,
                current_month
            )

        elif choice == "17":

            print(
                "\nThank you for using "
                "Smart Expense Tracker! 👋"
            )

            break

        else:

            print(
                "Invalid choice."
            )


# ==========================================
# START PROGRAM
# ==========================================

main()