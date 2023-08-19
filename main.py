app_name = "Jeatterey"
sales_tax = 1.0825
menu = {
    "sku1": { "name": "Adobo", "price": 5.99},
    "sku2": { "name": "Papaitan", "price": 7.99},
    "sku3": { "name": "Inihaw", "price": 5.99},
    "sku4": { "name": "Sinigang", "price": 7.99},
    "sku5": { "name": "Tinola", "price": 7.99},
    "sku6": { "name": "Sisig", "price": 5.99},
    "sku7": { "name": "Sinampalok", "price": 5.99}
}

options = { 
    1: "Add to cart",
    2: "Remove from cart",
    3: "Modify quantity",
    4: "View cart",
    5: "Checkout",
    6: "Exit"
}

cart = {}

"""
Functions:
* display_menu
* add_item
* remove_item
"""

def display_menu():
    print("\n**** Menu ****\n")
    for key in menu.keys():
        menu_num = key[3:]
        print(f"({menu_num}) {menu[key]['name']}: ${menu[key]['price']}")
    print("\n**************\n")

def add_to_cart(sku, quantity=1):
    if sku not in menu:
        print("Error: This item is not on the menu...\n")
    else:
        if sku in cart:
            cart[sku]["quantity"] += quantity
        else:
            cart[sku]= { "quantity": quantity, "name": menu[sku]['name'] }
        print(f"Added {quantity} of {cart[sku]['name']} to cart.\n")

def remove_from_cart(sku, quantity=1):
    success_code = 1
    if sku not in cart:
        print("Error: This item is not in your cart...\n")
    else:
        if (quantity==cart[sku]["quantity"]) or (cart[sku]["quantity"]==1):
            item_removed = cart.pop(sku)
        elif quantity>=1 and cart[sku]["quantity"] > quantity:
            cart[sku]["quantity"] -= quantity
            item_removed = cart[sku]
        else:
            print("Invalid quantity...\n")
            success_code = 0
            return success_code
        print(f"Removed: {quantity} of {item_removed['name']}, from cart.\n")
        return success_code

def modify_cart(sku, quantity):
    if sku in cart:
        remove_code = 1
        if quantity > 0:
            cart[sku]["quantity"] = quantity
        elif quantity < 0:
            remove_code = remove_from_cart(sku, abs(quantity))
        else:
            remove_code = remove_from_cart(sku, cart[sku]["quantity"])
        
        if remove_code:
            print(f"Modified {menu[sku]['name']} quantity to {quantity} in the cart.\n") 
    else:
        print("Invalid input. Item not in the cart...\n")

def view_cart():
    print("\n***** Cart *****")
    sub_total = 0
    for sku in cart:
        print(f"{cart[sku]['quantity']} x {cart[sku]['name']}")
        sub_total += menu[sku]["price"]*cart[sku]["quantity"]
    print(f"Total: ${format(sub_total*sales_tax,'.2f')}")
    print("****************\n")

def checkout():
    print("\n~~~~~ Checkout ~~~~~~")
    view_cart()
    print("Order submitted...\n")

# TODO Create flow
def main():
    print(f"----- {app_name}: Filipino Cuisine ~ -----")
    display_menu()
    add_to_cart("sku2",3)
    modify_cart("sku2",6)
    add_to_cart("sku3")
    add_to_cart("sku4",4)
    checkout()
if __name__ == "__main__":
    main()