app_name = "Jeatterey"
sales_tax = 0.0825
menu = { "products":[
    {"sku1": { "name": "Adobo", "price":"5.99"}},
    {"sku2": { "name": "Papaitan", "price":"7.99"}},
    {"sku3": { "name": "Inihaw", "price":"5.99"}},
    {"sku4": { "name": "Sinigang", "price":"7.99"}},
    {"sku5": { "name": "Tinola", "price":"7.99"}},
    {"sku6": { "name": "Sisig", "price":"5.99"}},
    {"sku7": { "name": "Sinampalok", "price":"5.99"}}
]}

options = { 
    1: "Add to cart",
    2: "Remove from cart",
    3: "Modify quantity",
    4: "View cart",
    5: "Checkout",
    6: "Exit"
}

cart = {}



def main():
    print(menu)

if __name__ == "__main__":
    main()