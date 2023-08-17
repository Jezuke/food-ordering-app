app_name = "Jeatterey"
sales_tax = 0.0825
menu = {
    "sku1": { "name": "Adobo", "price":"5.99"},
    "sku2": { "name": "Papaitan", "price":"7.99"},
    "sku3": { "name": "Inihaw", "price":"5.99"},
    "sku4": { "name": "Sinigang", "price":"7.99"},
    "sku5": { "name": "Tinola", "price":"7.99"},
    "sku6": { "name": "Sisig", "price":"5.99"},
    "sku7": { "name": "Sinampalok", "price":"5.99"}
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

def add_to_cart(sku, quantity):
    if sku not in menu:
        print("Error: This item is not on the menu...\n")
    else:
        if sku in cart:
            cart[sku]["quantity"] += quantity
        else:
            cart[sku]= { "quantity": quantity }
        print(f"Added {quantity} of {menu[sku]['name']} to cart.\n")

def main():
    print(f"----- {app_name}: Filipino Cuisine ~ -----")
    display_menu()
    # add_to_cart("sku22",1)

if __name__ == "__main__":
    main()