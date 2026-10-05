import matplotlib.pyplot as plt


# ==========================================
# CATEGORY CHART
# ==========================================

def show_category_chart(expenses):

    if len(expenses) == 0:

        print("No expenses available.")

        return

    categories = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    names = list(categories.keys())
    amounts = list(categories.values())

    plt.figure(figsize=(8, 5))

    plt.bar(
        names,
        amounts
    )

    plt.title(
        "Spending by Category"
    )

    plt.xlabel(
        "Category"
    )

    plt.ylabel(
        "Amount (₹)"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.show()


# ==========================================
# MONTHLY CHART
# ==========================================

def show_monthly_chart(expenses):

    if len(expenses) == 0:

        print("No expenses available.")

        return

    monthly_totals = {}

    for expense in expenses:

        expense_date = expense["date"]

        if expense_date == "Unknown":
            continue

        month = expense_date[:7]
        amount = expense["amount"]

        if month in monthly_totals:
            monthly_totals[month] += amount
        else:
            monthly_totals[month] = amount

    if len(monthly_totals) == 0:

        print(
            "No dated expenses available."
        )

        return

    months = sorted(
        monthly_totals.keys()
    )

    amounts = []

    for month in months:

        amounts.append(
            monthly_totals[month]
        )

    plt.figure(figsize=(8, 5))

    plt.bar(
        months,
        amounts
    )

    plt.title(
        "Monthly Spending"
    )

    plt.xlabel(
        "Month"
    )

    plt.ylabel(
        "Amount (₹)"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.show()


# ==========================================
# PIE CHART
# ==========================================

def show_category_pie_chart(expenses):

    if len(expenses) == 0:

        print("No expenses available.")

        return

    categories = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    names = list(categories.keys())
    amounts = list(categories.values())

    plt.figure(figsize=(7, 7))

    plt.pie(
        amounts,
        labels=names,
        autopct="%1.1f%%"
    )

    plt.title(
        "Expense Distribution"
    )

    plt.show()