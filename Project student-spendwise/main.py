def display_budget_status(expenses, budget):
    total_spent = sum(price for category in expenses.values() for price in category.values())
    print(f"Total spent: ${total_spent}")
    if budget is None:
        print("You have not set a budget yet.")
    elif total_spent > budget:
        print(f"Warning! Exceeded by ${total_spent - budget}.")
    else:
        print(f"Safe! You have ${budget - total_spent} left.")

expenses = {
    "Food":{},
    "Fun":{},
    "Bills":{},
    "Other":{}
}

print("Welcome to Student SpendWise")

while True:
    print("\n--- MAIN MENU ---")
    print("1. Add new expense")
    print("2. View expenses in category")
    print("3. Budget")
    print("4. Exit")
    choice = input("Please select an option (1, 2, 3, or 4): ")

    if choice == "1":
        available_categories = " , ".join([cat.capitalize() for cat in expenses.keys()])
        promt_text = f"What type of expense is this? ({available_categories}): "
        item_type = input(promt_text).capitalize()

        if item_type not in expenses:
            print("Invalid category. Please choose from Food, Fun, Bills, or Other.")
            continue
          

        item_name = input(f"What did you buy in {item_type}? ")

        try:
            price = int(input(f"How much for {item_name}? "))
            expenses[item_type][item_name] = price
        except ValueError:
            print("Please enter a valid number for the price.")
            continue
    
    elif choice == "2":
        category = input("Which category would you like to view? (Food, Fun, Bills, Other): ").capitalize()
        if category in expenses:
            print(f"Expenses in {category}:")
            for item, price in expenses[category].items():
                print(f"{item}: ${price}")
        else:
            print("Invalid category. Please choose from Food, Fun, Bills, or Other.")

    elif choice == "3":
        while True:
            print ("Do you want to plan, check or update your budget?")
            choice = input ("Type 'plan', 'check' or 'update': ").lower()
            if choice == 'plan':
                print("What is your budget for this month?")
                budget = input("Enter your budget: ")
            elif choice == 'check':
               display_budget_status(expenses, budget)
            elif choice == 'update':
               try:
            budget = int(input("Enter your updated budget: "))
            display_budget_status(expenses, budget)
            except ValueError:
            print("Invalid input. Please enter a number.")
                
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

while True:
    available_categories = " , ".join([cat.capitalize() for cat in expenses.keys()])
    promt_text = f"What type of expense is this? ({available_categories}) (or type 'stop' to exit): "
    item_type = input(promt_text)

    if item_type.lower() == 'stop': # Added .lower() to handle 'Stop' or 'STOP'
        break

    category = item_type.lower()
    
    if category not in expenses:
       expenses[category] = {} 
       print (f"Added new category: {category}")

    item_name = input(f"What did you buy in {category}? ")

    try:
        price = int(input(f"How much for {item_name}? "))
        expenses[category][item_name] = price
    except ValueError:
        print("Please enter a valid number for the price.")
        continue




print(f"Total spent: {sum(expenses.values())}")