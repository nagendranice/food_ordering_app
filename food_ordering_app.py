import random
import json
import time
import datetime
#Admin Module


# Dictionary to store the food items
menu = {}

# Dictionary to store the orders
orders = {}

menu_file_path = "menu.json"

        
# Function to add new food item to the menu
def add_food_item():
    food_id = str(random.randint(1000, 9999)) # Generate random food ID
    name = input("Enter the name of the food item: ")
    quantity = input("Enter the quantity of the food item (e.g. 100ml, 250gm, 4 pieces): ")
    price = float(input("Enter the price of the food item: "))
    discount = float(input("Enter the discount for the food item (in percentage): "))
    stock = int(input("Enter the amount left in stock for the food item: "))
    
    menu[food_id] = {
        "food_id":food_id,
        "name": name,
        "quantity": quantity,
        "price": price,
        "discount": discount,
        "stock": stock
    }
    print(menu)
        # Check if the item already exists in the JSON file
    with open(menu_file_path, 'r',encoding='utf-8') as f:
        items = json.loads(f.read())
        
        if name in items:
            print('Item with this name already exists.')
            return
    
    # Add new item to the JSON file
    with open('menu.json', 'w',encoding='utf-8') as f:
        json.dump(menu, f)
    print("Food item added successfully! Food ID:", food_id)
    print()

import json

def edit_food_menu():
    # Load the contents of the menu.json file into a dictionary
    with open('menu.json', 'r') as f:
        menu = json.load(f)
        
    # Prompt the user to enter the ID of the food item they want to edit
    food_id = input('Enter the ID of the food item you want to edit: ')
    
    # Check if the entered ID exists in the menu
    if food_id not in menu:
        print('Invalid ID. Try again.\n')
        edit_food_menu()
        return
    
    # Prompt the user to enter the new values for the food item
    print("Enter the new details of the food item: ")
    name = input("Name [" + menu[food_id]["name"] + "]: ") or menu[food_id]["name"]
    quantity = input("Quantity [" + menu[food_id]["quantity"] + "]: ") or menu[food_id]["quantity"]
    price = float(input("Price [" + str(menu[food_id]["price"]) + "]: ")) or menu[food_id]["price"]
    discount = float(input("Discount [" + str(menu[food_id]["discount"]) + "]: ")) or menu[food_id]["discount"]
    stock = int(input("Stock [" + str(menu[food_id]["stock"]) + "]: ")) or menu[food_id]["stock"]
    # Update the menu dictionary with the new values
    menu[food_id] = {
        'food_id':food_id,
        'name': name,
        'quantity': quantity,
        'price': price,
        'discount': discount,
        'stock': stock
    }
    
    # Write the updated dictionary to the menu.json file
    with open('menu.json', 'w') as f:
        json.dump(menu, f)
    
    print('Food item updated successfully.\n')

def view_menu():
    with open('menu.json', 'r') as f:
        menu = json.load(f)
    print('Menu:')
    for food in menu.values():
#         print(menu)
        print(f"{food['food_id']} - {food['name']}: {food['price']} Tk.")

def remove_food_item():
    with open('menu.json', 'r') as file:
        menu = json.load(file)
        
    food_id = input('Enter the ID of the food item to remove: ')
    for item in menu.values():
        if item['food_id'] == food_id:
            del menu[item['food_id']]
            with open('menu.json', 'w') as file:
                json.dump(menu, file, indent=2)
            print(f'Food item with ID {food_id} has been removed from the menu.\n')
            return
    
    print(f'No food item with ID {food_id} was found in the menu.\n')

def admin():
    print('Welcome, Admin!')
    password = input('Please enter your password: ')
    
    if password != 'admin123':
        print('Incorrect password. Try again.\n')
        admin()
    else:
        while True:
            print('What would you like to do?')
            print('(1) Add new food item')
            print('(2) Edit food item')
            print('(3) View all food items')
            print('(4) Remove food item')
            print('(E)xit')
            choice = input('Enter your choice: ')
            if choice == '1':
                add_food_item()
            elif choice == '2':
                edit_food_menu()
            elif choice == '3':
                view_menu()
            elif choice == '4':
                remove_food_item()
            elif choice == 'E':
                print('Returning to main menu.')
                main()
                return
            else:
                print('Invalid input. Try again.\n')


def generate_order_id():
    return f"ORD-{int(time.time())}-{random.randint(100, 999)}"

def login():
    print("Welcome")
    
    while True:
        print('What would you like to do?')
        print('(1) Register')
        print('(2) Login')
        print('(3) Exit')
        choice = input('Enter your choice: ')
        
        if choice == '1':
            register()
        elif choice == '2':
            name,user_id = customer_login()
            if name==None:
                name = customer_login()
            else:
                customer(user_id,name)
        elif choice == '3':
            print('Thank you for visiting our restaurant. Have a nice day!')
            return
        else:
            print('Invalid input. Try again.\n')
            
def customer(name,user_id):
    print('Welcome to our restaurant!')
    
    while True:
        print(f'What would you like to do, {user_id}?')
        print('(1) Place an order')
        print('(2) View menu')
        print('(3) Order History')
        print('(4) Update Profile')
        print('(5) Exit')
        choice = input('Enter your choice: ')
        
        if choice == '1':
            place_order(user_id)
        elif choice == '2':
            view_menu()
        elif choice == '3':
            view_order_history(user_id)
        elif choice == '4':
            update_profile(user_id)
        elif choice == '5':
            print('Thank you for visiting our restaurant. Have a nice day!')
            return
        else:
            print('Invalid input. Try again.\n')
            
def view_menu():
    try:
        with open('menu.json', 'r') as file:
            menu = json.load(file)
    except FileNotFoundError:
        print('Menu not found.')
        return
    
    print('Here is our menu:')
    for item in menu.values():
        print(f"{item['food_id']} - {item['name']}, {item['price']}$")
    print()
    
def place_order(user_id):
    try:
        with open('menu.json', 'r') as file:
            menu = json.load(file)
    except FileNotFoundError:
        print('Menu not found.')
        return
    
    print('Here is our menu:')
    for item in menu.values():
        print(f"{item['food_id']} - {item['name']}, {item['price']}₹")
    print()
    
    order_id = generate_order_id()
    order_date = str(datetime.datetime.today())
    items = []
    order = []
    total_amount = 0.0
    
    while True:
        food_id = input('Enter food item id (Enter "done" to finish): ')
        if food_id == 'done':
            break
        
        if food_id not in menu:
            print('Invalid food item id. Try again.\n')
            continue
        
        quantity = int(input('Enter quantity: '))
        if quantity > menu[food_id]['stock']:
            print('Insufficient stock. Try again.\n')
            continue
        
        name = menu[food_id]['name']
        price = menu[food_id]['price']
        discount = menu[food_id]['discount']
        subtotal = (price * quantity) * (1 - discount / 100)
        total_amount += subtotal
        
        # Add the food item to the order
        item = {
            'food_id': food_id,
            'name': name,
            'quantity': quantity,
            'price': price,
            'discount': discount,
            'subtotal': subtotal
        }
        items.append(item)
        order.append(item)
        # Update the stock of the food item
        menu[food_id]['stock'] -= quantity
        
        print(f"{quantity} {item['name']} added to your order. Subtotal: {item['subtotal']}$\n")
    
    print('Here is your order:')
    for item in order:
        print(f"{item['quantity']} x {item['name']} = {item['subtotal']}$")
    print(f"Total price: {total_amount}$\n")
    
    # Save the order details to the orders.json file
    order_data = {
        'user_id': user_id,
        'order_id': order_id,
        'order_date': order_date,
        'total_amount': total_amount,
        'items': items
    }
    
    try:
        with open('orders.json', 'r') as f:
            orders = json.load(f)
    except FileNotFoundError:
        orders = {}
        
    orders[order_id] = order_data
    
    with open('orders.json', 'w') as f:
        json.dump(orders, f,indent=4)
    with open('menu.json','w') as f:
        json.dump(menu,f,indent=4)
    
    print(f'\nOrder placed successfully. Your order id is {order_id}!')


def customer_login():
    print('--- Customer Login ---')
    user_id = input('userid: ')
    password = input('Password: ')

    with open('users.json') as f:
        users = json.load(f)

    if user_id in users and users[user_id]['password'] == password:
        print(f'Welcome, {users[user_id]["full_name"]}!')
        return user_id,users[user_id]['full_name']
    else:
        print('Invalid email or password. Please try again.')
        return None,None

def register():
    print('--- Register ---')
    with open('users.json', 'r') as f:
        users = json.load(f)

    # Generate user ID
    if len(users) == 0:
        user_id = 1
    else:
        user_id = users[-1]['user_id'] + 1

    # Get user details
    full_name = input('Enter your full name: ')
    phone_number = input('Enter your phone number: ')
    email = input('Enter your email address: ')
    address = input('Enter your address: ')
    password = input('Enter your password: ')

    # Add user to users list
    user = {
        'user_id': user_id,
        'full_name': full_name,
        'phone_number': phone_number,
        'email': email,
        'address': address,
        'password': password,
        'order_history': []
    }
    users[user_id] = user

    # Write updated users list to file
    with open('users.json', 'w') as f:
        json.dump(users, f)

    print(f'Registration successful and your user_id is {user_id}')
import json

def view_order_history(user_id):
    try:
        with open('orders.json') as f:
            orders = json.load(f)
            
        user_orders = [order for order in orders.values() if order['user_id'] == user_id]
        
        if len(user_orders) == 0:
            print("You haven't made any orders yet.")
        else:
            print("Your order history:")
            for order in user_orders:
                print(f"Order ID: {order['order_id']}, Order Date: {order['order_date']}, Total Amount: {order['total_amount']}")
                for item in order['items']:
                    print(f"- {item['name']}: {item['quantity']} x {item['price']} = {item['quantity']*item['price']}")
                print()
    except FileNotFoundError:
        print('No orders found.')

def update_profile(user_id):
    try:
        with open('users.json') as f:
            users = json.load(f)
    except FileNotFoundError:
        print('User file not found.')
        return
    
    for user in users.values():
        if user['user_id'] == user_id:
            print(f"Your current profile information: Name: {user['full_name']}, Phone: {user['phone_number']}, Email: {user['email']}, Address: {user['address']}")
            
            full_name = input("Enter your name (press enter to keep current): ")
            if full_name:
                user['full_name'] = full_name
                
            phone_number = input("Enter your phone number (press enter to keep current): ")
            if phone_number:
                user['phone_number'] = phone_number
                
            email = input("Enter your email (press enter to keep current): ")
            if email:
                user['email'] = email
                
            address = input("Enter your address (press enter to keep current): ")
            if address:
                user['address'] = address
            
            with open('users.json', 'w') as f:
                json.dump(users, f)
            
            print("Profile updated successfully.")
            break
    else:
        print("User not found.")

def main():
    print('Welcome to the Restaurant')
    print('Are you a customer or an admin?')
    print('(C)ustomer\n(A)dmin\n(E)xit')
    choice = input('Enter your choice: ')
    
    if choice == 'C':
        login()
    elif choice == 'A':
        admin()
    elif choice == 'E':
        print('Thank you for visiting!')
        return
    else:
        print('Invalid input. Try again.\n')
        main()

if __name__ == '__main__':
    main()
