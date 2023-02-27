
cart = {}

heat = {
    'Sneakers': {
        'Yeezy',
        'Nike',
        'New balance',
    },
    'T-shirts': {
        'V-Lone',
        'Astroworld',
        'Bluevine',
    },
    'Snacks': {
        'Doritoes',
        'Oreos',
        'Rap Snacks',
    },
}

while True:
    print(heat["Sneakers"])
    print(heat["T-shirts"])
    print(heat["Snacks"])
   
   
    print("""
    Shopping Cart Options
    ------------------------
    1: Add item
    2: Remove item
    3: View cart
    0: Quit program
    """)

    ask_in = input("Enter your choice: ")

    if ask_in == "1":
        item = input("Enter the item you want to add: ")
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
        print(f"{item} added to cart.")
        


    elif ask_in == "3":
        print("Your shopping cart:")
        for item, quantity in cart.items():
            print(f"{quantity} x {item}")
        print()

    elif ask_in == "0":
        print("Thank you for shopping with us!")
        print("Here is your receipt:")
        for item, quantity in cart.items():
            print(f"{quantity} x {item}")
        break
    else:
        print("Invalid ask_in. Please try again.")
        print()