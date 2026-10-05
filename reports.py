# ==========================================
# REPORT FUNCTIONS
# ==========================================


def calculate_average(expenses):

    if len(expenses) == 0:
        return 0

    total = 0

    for expense in expenses:
        total += expense["amount"]

    average = total / len(expenses)

    return average


# ==========================================
# HIGHEST EXPENSE
# ==========================================

def get_highest_expense(expenses):

    if len(expenses) == 0:
        return None

    highest = expenses[0]

    for expense in expenses:

        if expense["amount"] > highest["amount"]:
            highest = expense

    return highest


# ==========================================
# TOP CATEGORY
# ==========================================

def get_top_category(expenses):

    if len(expenses) == 0:
        return None

    categories = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    top_category = max(
        categories,
        key=categories.get
    )

    return top_category


# ==========================================
# CATEGORY TOTALS
# ==========================================

def get_category_totals(expenses):

    categories = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    return categories


# ==========================================
# MONTHLY TOTAL
# ==========================================

def get_monthly_total(expenses, month):

    total = 0

    for expense in expenses:

        if expense["date"].startswith(month):

            total += expense["amount"]

    return total


# ==========================================
# DASHBOARD
# ==========================================

def show_dashboard(expenses, budget, current_month):

    print("\n")
    print("=" * 45)
    print("          SMART EXPENSE DASHBOARD")
    print("=" * 45)

    if len(expenses) == 0:

        print("\nNo expenses available.")
        return

    # Total spending

    total = 0

    for expense in expenses:
        total += expense["amount"]

    # Average

    average = calculate_average(expenses)

    # Highest expense

    highest = get_highest_expense(expenses)

    # Top category

    top_category = get_top_category(expenses)

    # Current month spending

    monthly_total = get_monthly_total(
        expenses,
        current_month
    )

    # Budget percentage

    if budget > 0:

        budget_percentage = (
            monthly_total / budget
        ) * 100

        remaining = budget - monthly_total

    else:

        budget_percentage = 0
        remaining = 0

    print(
        f"\nTotal Spending      : ₹{total:.2f}"
    )

    print(
        f"Number of Expenses  : {len(expenses)}"
    )

    print(
        f"Average Expense     : ₹{average:.2f}"
    )

    print(
        f"Highest Expense     : ₹{highest['amount']:.2f}"
    )

    print(
        f"Top Category        : {top_category}"
    )

    print(
        f"\nCurrent Month       : {current_month}"
    )

    print(
        f"Monthly Budget      : ₹{budget:.2f}"
    )

    print(
        f"Spent This Month    : ₹{monthly_total:.2f}"
    )

    print(
        f"Remaining Budget    : ₹{remaining:.2f}"
    )

    print(
        f"Budget Used         : {budget_percentage:.2f}%"
    )

    print("=" * 45)