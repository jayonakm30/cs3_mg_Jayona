def calculate_total(topping_count):
    base_price = 10.00
    topping_price = 1.50
    return base_price + topping_count * topping_price

valid_toppings = ["pepperoni", "mushroom", "extra cheese"]
topping_count = 0

while True: 
    choice = input("Enter your choice of toppings or enter done to stop")

    if choice == "done":
        break
    if choice == "pepperoni":
        print("added pepperoni")

    if choice == "mushroom":
            print("added mushroom")

    if choice == "extra cheese":
                print("added extra cheese")

    else:
          print("Not in menu")

final_bill = calculate_total(topping_count)
print(f"\nYour total bill is {10 + topping_count * 1.50}")