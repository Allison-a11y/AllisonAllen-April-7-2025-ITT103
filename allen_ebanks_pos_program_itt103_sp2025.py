#The product catalog containing the items we offer
product_catalog = {
  "Electronics":
  {

  "Vacuum Cleaner": {"price": 25000.00, "stock": 10},

  "Refridgerator": {"price": 30000.00, "stock": 25},

  "Laundry Machine": {"price": 40000.00, "stock": 15},

  "Coffee Maker": {"price": 10000.00, "stock": 30},

  "Dish Washer": {"price": 20000.00, "stock": 50},

  "Microwave": {"price": 15000.00, "stock": 40},
  },

  "Non-Electronics":
  {
  "Mop": {"price": 300.00, "stock": 60},

  "Broom": {"price": 350.00, "stock": 20},

  "Iron Board": {"price": 200.00, "stock": 12},

  "Pot": {"price": 500.00, "stock": 18}
  },

  "Liqour":
  {

  "Sminoff Vodka": {"price": 1200.00, "stock": 10},

  "RedStripe Beer": {"price": 250.00, "stock": 25},

  "Guiness": {"price": 300.00, "stock": 15},

  "Wine": {"price": 1100.00, "stock": 30},
  },

  "Beverages":
  {

  "Cream Soda": {"price": 150.00, "stock": 60},

  "Fruit Punch Drinks": {"price": 100.00, "stock": 20},

  "Sergen Island Milk": {"price": 150.00, "stock": 12},

  "Natural Fruit Punch": {"price": 300.00, "stock": 18},

  "Starbucks Coffee": {"price": 400.00, "stock": 50},

  "Orange Juice": {"price": 100.00, "stock": 40},
  },

  "Groceries":
  {

  "National Bread": {"price": .00, "stock": 10},

  "HTB Bun": {"price": 100.00, "stock": 25},

  "Body Wash": {"price": 350.00, "stock": 15},

  "Shampoo": {"price": 400.00, "stock": 30},

  "Conditioner": {"price": 450.00, "stock": 60},

  "Bagged Rice": {"price": 250.00, "stock": 20},

  "Mixed Parts": {"price": 150.00, "stock": 12},

  "Tin Cheese": {"price": 1100.00, "stock": 18},

  "Stick Butter": {"price": 150.00, "stock": 50},

  "Mixed Fruits": {"price": 500.00, "stock": 40},
  }

  }

#Function to view the catalog
def display_product(product_catalog):
  for category, items in product_catalog.items():
    print(f"\n{category.capitalize()}: ")
    for item, details in items.items():
      print(f"\n{item}: Price: ${details['price']} Stock: {details['stock']}")

#Function to remove a product
def remove_product(product_catalog):
  product_name = input("Enter the product name to remove: ")
  found = False
  for category, products in product_catalog.items():
    if product_name in products:
      del products[product_name]
      print(f"{product_name} has been removed.")
      found = True
      break
  if not found:
      print("Product not found.")

#Function to add a product
def add_product(product_catalog):
  print("Categories are Non-Electronic, Electronis, Liqour, Beverages, Groceries: ")
  category= input("Enter category name")
  if category not in product_catalog:
    print("Incorrect Category")
    return
  else:
    product_name = input("Enter the new product name: ")
    if product_name in product_catalog[category]:
      print("Product already exists.")
    else:
      try:
        stock = int(input("Please enter the stock amount"))
        price = float(input("Please enter the price amount"))
        product_catalog[category][product_name] = {"price": price,"stock": stock}
        print(f"product name: {product_name}, price: {price}, stock: {stock} was added successfully!")
      except ValueError:
        print("There is an Error with input")

#Function to update a product
def update_product(product_catalog):
  print("Categories are Non-Electronic, Electronis, Liqour, Beverages, Groceries: ")
  category= input("Enter category name")
  if category not in product_catalog:
    print("Incorrect Category")
    return
  else:
    product_name = input("Enter the product name to update stock: ")
    if product_name in product_catalog[category]:
      try:
          stock = int(input("Enter the amount you wish to add: "))
          if stock < 0:
              print("Invalid input.")
          else:
              product_catalog[category][product_name]["stock"] += stock
              print(f"Updated stock for {product_name}: {product_catalog[category][product_name]['stock']}")
      except ValueError:
          print("Invalid input. Please enter an integer value.")

"""Function for add the product(s):
to select the items to purchase
to allow the cashier to enter the amt received from customer
to display subtotal, cash received, the tax, total due, the change"""

def purchase_product(product_catalog):
    purchases = []
    subtotal = 0
    discount = 0
    total_amt = 0

    while True:
        choice = input("\nWould you like to make a purchase? (yes/no): ").lower()

        if choice == "no":
            if subtotal == 0:
                print("\nNo purchase was made.\nThank you for visiting Best Buy Retail Store.")
            else:
                if subtotal > 5000:
                    discount = subtotal * 0.05

                tax = (subtotal - discount) * 0.10
                total_amt = subtotal - discount + tax

                # To re-enter cash
                while True:
                    try:
                        customer_amt = float(input("Please enter cash: $"))
                        if customer_amt >= total_amt:
                            change = customer_amt - total_amt
                            print("\n************************************Receipt************************************")
                            for item in purchases:
                                print(f"{item['product']} x{item['quantity']} - ${item['total']:.2f}")
                            if discount > 0:
                                print(f"\nDiscount (5%): -${discount:.2f}")
                            print(f"Subtotal: ${subtotal:.2f}")
                            print(f"Tax (10%): ${tax:.2f}")
                            print(f"Total Due: ${total_amt:.2f}")
                            print(f"Cash Received: ${customer_amt:.2f}")
                            print(f"Change: ${change:.2f}")
                            print("************************************Receipt************************************")
                            print("Thank You For Shopping at Best Buy Retail Store")
                            break  #Exit the loop
                        else:
                            print("Insufficient funds. Please enter a valid amount.")
                    except ValueError:
                        print("Invalid input. Please enter a valid cash amount.")
            break  # Exit the loop for cashing the product

        elif choice == "yes":
            print("\nAvailable categories: Electronics, Non-Electronics, Liqour, Beverages, Groceries")
            category = input("Enter category name: ")

            if category not in product_catalog:
                print("Incorrect Category.")
                continue

            product_name = input("Enter the product name to purchase: ")
            found_product = None

            for name in product_catalog[category]:
                if name.lower() == product_name.lower():
                    found_product = name
                    break

            if found_product:
                try:
                    quantity = int(input("Enter the quantity to purchase: "))
                    if quantity <= 0:
                        print("Invalid quantity. Must be greater than zero.")
                    elif quantity > product_catalog[category][found_product]['stock']:
                        print("Not enough stock available.")
                    else:
                        total_cost = quantity * product_catalog[category][found_product]['price']
                        product_catalog[category][found_product]['stock'] -= quantity
                        subtotal += total_cost

                        purchases.append({
                            "product": found_product,
                            "quantity": quantity,
                            "total": total_cost
                        })

                        print(f"You purchased {quantity} {found_product}(s) for ${total_cost:.2f}.")
                        print(f"Remaining stock: {product_catalog[category][found_product]['stock']}")

                        if product_catalog[category][found_product]['stock'] <= 5:
                            print("Stock is low. Please restock the product.")
                except ValueError:
                    print("Invalid input. Please enter a valid quantity.")
            else:
                print("Product not found.")
        else:
            print("Please type 'yes' or 'no'.")

"""
The  login for the user (whether manager or cashier)
The menu options for when you want to select view, remove, etc
"""
i = 1
log_in = False

while i <= 3 and not log_in:
    print("\n**************************************************************************")
    print("****Welcome****")
    print("Best Buy Retail Store")
    print("Log In Screen")
    print("Please enter user information")
    print("****************************************************************************")
    try:
        username = input("Username: ")
        password = input("Password: ")

        if not username.isalpha():
            print("Invalid entry. Username must contain only letters.")
            i += 1
            if i > 3:
                print("Too many attempts. Exiting system.")
        else:
            print("Login successful")
            log_in = True

            while log_in:
                try:
                    option = int(input("\nEnter 1 - Manager, 2 - Cashier, 0 - Exit: "))

                    if option == 1:
                        print("\nWelcome Manager")

                        while True:
                            print("\nManager Menu:")
                            print("1 - View product")
                            print("2 - Remove product(s)")
                            print("3 - Add product(s)")
                            print("4 - Update stock")
                            print("5 - Customer purchasing")
                            print("0 - Logout")

                            choice = int(input("Enter menu option: "))

                            if choice == 1:
                                display_product(product_catalog)
                            elif choice == 2:
                                remove_product(product_catalog)
                            elif choice == 3:
                                add_product(product_catalog)
                            elif choice == 4:
                                update_product(product_catalog)
                            elif choice == 5:
                                purchase_product(product_catalog)
                            elif choice == 0:
                                print("Logging out...\n")
                                log_in = False
                                break
                            else:
                                print("Invalid menu option")

                    elif option == 2:
                        print("\nWelcome Cashier")

                        while True:
                            print("\nCashier Menu:")
                            print("1 - View product(s)")
                            print("2 - Remove product(s)")
                            print("3 - Add product")
                            print("4 - Customer Purchase")
                            print("0 - Logout")

                            choice = int(input("Enter menu option: "))

                            if choice == 1:
                                display_product(product_catalog)
                            elif choice == 2:
                                remove_product(product_catalog)
                            elif choice == 3:
                                add_product(product_catalog)
                            elif choice == 4:
                                purchase_product(product_catalog)
                            elif choice == 0:
                                print("Logging out...\n")
                                log_in = False
                                break
                            else:
                                print("Invalid menu option")

                    elif option == 0:
                        print("Exiting system...")
                        log_in = False

                    else:
                        print("Invalid Input")

                except ValueError:
                    print("Please enter a valid number")

    except ValueError:
        print("Invalid input. Try again.")