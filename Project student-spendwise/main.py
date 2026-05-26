import json

expenses = {
    "Food": {},
    "Fun": {},
    "Bills": {},
    "Other": {}
}
budget = 0

# FUNCTIONS 

def calculate_total_spent(expenses_dict):
    """Calculates the total amount spent across all categories."""
    return sum(price for category in expenses_dict.values() for price in category.values())

def display_budget_status(expenses_dict, current_budget):
    """Displays the current budget status, including total spent and remaining budget."""
    total_spent = calculate_total_spent(expenses_dict)
    print(f"\nTotal spent: ${total_spent}")
    if current_budget == 0:
        return "You have not set a budget yet."
    elif total_spent > current_budget:
        return f"Warning! You have exceeded your budget by ${total_spent - current_budget}."
    else:
        return f"Safe! You have ${current_budget - total_spent} left in your budget."

def save_data(expenses, budget, filename="data.json"):
    """Saves current expenses and budget to a JSON file."""
    try:
        data = {
            "expenses": expenses,
            "budget": budget
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except Exception:
        return False

def load_data(filename="data.json"):
    """Loads expenses and budget from a file. If the file doesn't exist, returns an empty structure."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("expenses"), data.get("budget", 0)
    except FileNotFoundError:
        default_expenses = {"Food": {}, "Fun": {}, "Bills": {}, "Other": {}}
        return default_expenses, 0
    
def delete_expense(expenses, category, item_name):
    """Deletes a specific expense from the selected category."""
    if category in expenses and item_name in expenses[category]:
        del expenses[category][item_name]
        return True
    return False

def add_new_category(expenses, category_name):
    """Adds a new expense category if it doesn't already exist."""
    category_name = category_name.strip().capitalize()
    if category_name and category_name not in expenses:
        expenses[category_name] = {}
        return True
    return False

def clear_all_data(expenses):
    """Clears all items within categories, but keeps the categories themselves."""
    for category in expenses:
        expenses[category].clear()

def get_category_total(expenses, category):
    """Returns the total amount spent in a specific category."""
    if category in expenses:
        return sum(expenses[category].values())
    return 0


# --- MAIN PROGRAM ---

print("Welcome to Student SpendWise")
expenses, budget = load_data()

while True:
    print("\n--- MAIN MENU ---")
    print("1. Add new expense")
    print("2. View expenses in category")
    print("3. Budget Management")
    print("4. Save and Exit")
    
    choice = input("Please select an option (1, 2, 3, or 4): ").strip()

    if choice == "1":
        available_categories = ", ".join([cat.capitalize() for cat in expenses.keys()])
        prompt_text = f"What type of expense is this? ({available_categories}): "
        item_type = input(prompt_text).strip().capitalize()

        if item_type not in expenses:
            print("Invalid category. Please choose from the available list.")
            continue

        item_name = input(f"What did you buy in {item_type}? ").strip()

        try:
            price = float(input(f"How much for {item_name}? "))
            if price < 0:
                print("Price cannot be negative.")
                continue
            expenses[item_type][item_name] = price
            print(f"Successfully added ${price} to {item_type}!")
        except ValueError:
            print("Please enter a valid number for the price.")
    
    elif choice == "2":
        available_categories = ", ".join([cat.capitalize() for cat in expenses.keys()])
        category = input(f"Which category would you like to view? ({available_categories}): ").strip().capitalize()
        if category in expenses:
            print(f"\nExpenses in {category}:")
            if not expenses[category]:
                print("No expenses in this category yet.")
            for item, price in expenses[category].items():
                print(f" - {item}: ${price}")
            print(f"Total for {category}: ${get_category_total(expenses, category)}")
        else:
            print("Invalid category.")

    elif choice == "3":
        print("\nDo you want to plan, check or update your budget?")
        budget_choice = input("Type 'plan', 'check' or 'update': ").strip().lower()
        
        if budget_choice == 'plan' or budget_choice == 'update':
            try:
                budget = float(input("Enter your budget amount: "))
                print(f"Budget updated to ${budget}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif budget_choice == 'check':
            status = display_budget_status(expenses, budget)
            print(status)
        else:
            print("Invalid option selected.")
                
    elif choice == "4":
        if save_data(expenses, budget):
            print("Data saved successfully to data.json!")
        else:
            print("Error saving data.")
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")