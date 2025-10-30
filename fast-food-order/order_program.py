import json

TAX_RATE = 0.07

def load_menu(filename="menu.json"):
    with open(filename, 'r') as f:
        return json.load(f)

def display_menu(menu):
    print("\n--- Menu ---")
    print("Main Food Items:")
    for i, item in enumerate(menu["main_food"]):
        print(f"{i + 1}. {item['name']} - ${item['price']:.2f}")
    print("\nSide Items:")
    for i, item in enumerate(menu["side_items"]):
        print(f"{i + 1}. {item['name']} - ${item['price']:.2f}")
    print("\nDrinks:")
    for i, item in enumerate(menu["drinks"]):
        print(f"{i + 1}. {item['name']} - ${item['price']:.2f}")

def get_choice(prompt, items):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(items):
                return items[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    menu = load_menu()

    print("Welcome to the Fast Food Restaurant!")
    user_name = input("Please enter your name: ")

    display_menu(menu)

    main_food_choice = get_choice("Select your main food item: ", menu["main_food"])
    side_item_choice = get_choice("Select your side item: ", menu["side_items"])
    drink_choice = get_choice("Select your drink: ", menu["drinks"])

    order_items = [main_food_choice, side_item_choice, drink_choice]
    subtotal = sum(item['price'] for item in order_items)
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print("\n--- Your Order Summary ---")
    print(f"Customer Name: {user_name}")
    for item in order_items:
        print(f"- {item['name']}: ${item['price']:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

    while True:
        payment_method = input("Preferred payment method (C for Cash, R for Credit): ").upper()
        if payment_method in ['C', 'R']:
            break
        else:
            print("Invalid payment method. Please enter C or R.")

    if payment_method == 'C':
        while True:
            try:
                cash_payment = float(input("Enter cash payment amount: $"))
                if cash_payment >= total:
                    change = cash_payment - total
                    print(f"Amount Paid: ${cash_payment:.2f}")
                    print(f"Change Due: ${change:.2f}")
                    break
                else:
                    print("Payment is less than total. Please enter sufficient amount.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
    else:
        print(f"Amount Charged to Credit: ${total:.2f}")

    print("\nThank you for your order!")

if __name__ == "__main__":
    main()
