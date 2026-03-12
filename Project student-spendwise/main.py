expenses = {}

print("--- Welcome to Student SpendWise ---")

while True:
    
    item = input("What did you buy? (or type 'stop' to exit): ")
    if item.lower() == 'stop': # Added .lower() to handle 'Stop' or 'STOP'
        break
    
    price = int(input("How much did it cost? "))
    
    # Adding the item and price to our dictionary
    expenses[item] = price


print(f"Total spent: {sum(expenses.values())}")