expenses = {
    "Food":{},
    "Fun":{},
    "Bills":{},
    "Other":{}
}

print("Welcome to Student SpendWise")

while True:
    item_type = input("What type of expense is this? (Food, Fun, Bills, Other) (or type 'stop' to exit): ")
    if item_type.lower() == 'stop': # Added .lower() to handle 'Stop' or 'STOP'
        break
    item = input("What did you buy? (or type 'stop' to exit): ")
    if item.lower() == 'stop': # Added .lower() to handle 'Stop' or 'STOP'
        break
    
    price = int(input("How much did it cost? "))
    
    # Adding the item and price to our dictionary
    expenses[item] = price




print(f"Total spent: {sum(expenses.values())}")