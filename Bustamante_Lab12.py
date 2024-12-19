foodmenu = {
    "Burger": 100,
    "Pizza": 350,
    "Pasta": 150,
    "Fries": 100
}

print("Welcome to JolClaud!")
print("Here is the menu:")
for item, price in foodmenu.items():
    print(f"{item}: ₱{price:.2f}")

selected_item = None
item_cost = 0.0

while True:
    print("\nPlease select your choice from the menu (type the name exactly as shown):")
    user_input = input()
    
    if user_input in foodmenu:
        selected_item = user_input
        item_cost = foodmenu[user_input]
        print(f"You have selected: {selected_item} - ${item_cost:.2f}")
        break
    else:
        print("Invalid selection. Please try again.")

while True:
    print(f"\nThe total cost is: ₱{item_cost:.2f}")
    print("Enter the amount of money you are giving please:")
    try:
        cash_rendered = float(input())
        
        if cash_rendered >= item_cost:
            change = cash_rendered - item_cost
            print(f"Payment accepted. Your change is: ₱{change:.2f}")
            break
        else:
            print(f"Insufficient cash. You need at least ₱{item_cost:.2f}. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric amount.")

print("\nThank you for your order! Enjoy your meal.")
