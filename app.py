import time
import main, os, sys
from main import GET_SALES_BY_ID, GET_SALES_BY_RATING, GET_SALES_BY_SALES
import sqlite3

MENU_PROMPT = """

COURTICECORP SALES MANAGER

Please choose one of the following options:
1) Add a new product
2) View all products
3) Search for a product
4) Get the best preparation method for a product
5) Delete a product
6) Edit a product
7) Exit

Your selection:
"""

SORT_PROMPT = """
Sort by:
1) Name (alphabetically
2) Rating (highest to lowest)
3) ID (lowest to highest)
4) Sales (highest to lowest)
5) Year (oldest to newest)
6) Return to main menu

Your selection:
"""

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    connection = main.connect()
    main.create_table(connection)

    while (user_input := input(MENU_PROMPT)) != "7":
        if user_input == "1":
            add_product(connection)
        elif user_input == "2":
            while (sort_input := input(SORT_PROMPT)) not in ["1", "2", "3", "4", "5", "6"]:
                print("Invalid input, please try again.")
            sorted_beans = main.sort_sales(connection, sort_input)
            for bean in sorted_beans:
                print(f"- ID {bean[0]}: {bean[1]} ({bean[2]}) - {bean[3]}/100 - {bean[4]} sales")
            input("Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif user_input == "3":
            search_for_product(connection)
        elif user_input == "4":
            get_best_prep(connection)
        elif user_input == "5":
            delete_bean(connection)
        elif user_input == "6":
            edit_product(connection)
        else:
            print("Invalid input, please try again.")
        os.system('cls' if os.name == 'nt' else 'clear')

def add_product(connection):
    name = input("Enter the name of the product: ")
    method = input("Enter the product year: ")
    rating = int(input("Enter the rating for this product (0-100): "))
    sales = int(input("Enter the number of sales for this product: "))
    main.add_sale(name, method, rating, sales)

def edit_product(connection):
    while True:
        try: 
            bean_id = int(input("Enter the ID of the product you want to edit: "))
            main.GET_SALES_BY_ID(connection, bean_id)
            if bean_id not in [sale[0] for sale in main.get_all_sales(connection)]:
                raise ValueError
            break
        except ValueError:
            print("Invalid ID, please try again.")

    name = input("Enter the new name of the product (leave blank to keep current): ")
    method = input("Enter the new product year: ")
    while True:
        try:
            
            rating = int(input("Enter the new rating for this product (0-100): "))
            main.GET_SALES_BY_RATING(connection, rating)
        except ValueError:
            rating = ""
            break
        else:
            break

    while True:
        try:
            sales = int(input("Enter the new number of sales for this product: "))
            main.GET_SALES_BY_SALES(connection, sales)
        except ValueError:
            sales = ""
            break
        else:
            break

    if name == "":
        name = main.GET_SALES_BY_ID(connection, bean_id)[1]
    if method == "":
        method = main.GET_SALES_BY_ID(connection, bean_id)[2]
    if rating == "":
        rating = main.GET_SALES_BY_ID(connection, bean_id)[3]
    if sales == "":
        sales = main.GET_SALES_BY_ID(connection, bean_id)[4]

    main.edit_sale(connection, bean_id, name, method, rating, sales)

def view_all_sales(connection):
    sales = main.get_all_sales(connection)
    for sale in sales:
        print(f"- ID {sale[0]}: {sale[1]}")
    
def search_for_product(connection):
    name = input("Enter the name of the product you want to search for: ")
    sales = main.get_sales_by_name(connection, name)
    for sale in sales:
        print(f"- {sale[1]} ({sale[2]}) - {sale[3]}/100")

def get_best_prep(connection):
    name = input("Enter the name of the product you want to find the best preparation method for: ")
    best_prep = main.get_best_prep(connection, name)
    print(f"The best preparation method for {name} is {best_prep[2]}.")

def delete_bean(connection):
    name = input("Enter the name of the product you want to delete: ")
    bean_id = input("Enter the ID of the product you want to delete: ")
    main.delete_sale(connection, name, bean_id)





print("""
    _____                 _   _           _____                 
  / ____|               | | (_)         / ____|                
 | |     ___  _   _ _ __| |_ _  ___ ___| |     ___  _ __ _ __  
 | |    / _ \| | | | '__| __| |/ __/ _ \ |    / _ \| '__| '_ \ 
 | |___| (_) | |_| | |  | |_| | (_|  __/ |___| (_) | |  | |_) |
  \_____\___/ \__,_|_|   \__|_|\___\___|\_____\___/|_|  | .__/ 
                                                        | |    
                                                        |_|    """)
input("Press Enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')
print("""
  _                 _ _               
 | |               | (_)              
 | | ___   __ _  __| |_ _ __   __ _   
 | |/ _ \ / _` |/ _` | | '_ \ / _` |  
 | | (_) | (_| | (_| | | | | | (_| |_ 
 |_|\___/ \__,_|\__,_|_|_| |_|\__, (_)
                               __/ |  
                              |___/   """)
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("""  _                 _ _                 
 | |               | (_)                
 | | ___   __ _  __| |_ _ __   __ _     
 | |/ _ \ / _` |/ _` | | '_ \ / _` |    
 | | (_) | (_| | (_| | | | | | (_| |_ _ 
 |_|\___/ \__,_|\__,_|_|_| |_|\__, (_|_)
                               __/ |    
                              |___/     """)
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("""
  _                 _ _                   
 | |               | (_)                  
 | | ___   __ _  __| |_ _ __   __ _       
 | |/ _ \ / _` |/ _` | | '_ \ / _` |      
 | | (_) | (_| | (_| | | | | | (_| |_ _ _ 
 |_|\___/ \__,_|\__,_|_|_| |_|\__, (_|_|_)
                               __/ |      
                              |___/       """) 
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
menu()