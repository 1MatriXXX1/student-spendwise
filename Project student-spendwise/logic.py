
def calculate_total_spent(expenses):
    """Calculates the total amount of all expenses."""
    return sum(sum(cat.values()) for cat in expenses.values())

def check_budget_status(total_spent, budget):
    """Returns the budget status and the remaining/exceeded difference."""
    if budget is None or budget == 0:
        return "No budget set", 0
    
    remaining = budget - total_spent
    if remaining >= 0:
        return "Safe", remaining
    else:
        return "Warning", abs(remaining)

def add_expense(expenses, category, item_name, price):
    """Adds a new expense item to the data structure."""
    if category in expenses:
        expenses[category][item_name] = price
        return True
    return False