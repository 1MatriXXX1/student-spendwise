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
    print("3. Exit")
    choice = input("Please select an option (1, 2, or 3): ")
    

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