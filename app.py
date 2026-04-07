import main, os, sys

MENU_PROMPT = """

Please choose one of the following options:
1) Add a new bean
2) View all beans
3) Search for a bean
4) Get the best preparation method for a bean
5) Delete a bean
6) Exit

Your selection:
"""

SORT_PROMPT = """
Sort by:
1) Name (alphabetically
2) Rating (highest to lowest)
3) ID (lowest to highest)
4) Return to main menu

Your selection:
"""

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    connection = main.connect()
    main.create_table(connection)

    while (user_input := input(MENU_PROMPT)) != "6":
        if user_input == "1":
            add_bean(connection)
        elif user_input == "2":
            while (sort_input := input(SORT_PROMPT)) not in ["1", "2", "3"]:
                print("Invalid input, please try again.")
            sorted_beans = main.sort_beans(connection, sort_input)
            for bean in sorted_beans:
                print(f"- ID {bean[0]}: {bean[1]} ({bean[2]}) - {bean[3]}/100")
            input("Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif user_input == "3":
            search_for_bean(connection)
        elif user_input == "4":
            get_best_prep(connection)
        elif user_input == "5":
            delete_bean(connection)
        else:
            print("Invalid input, please try again.")
        os.system('cls' if os.name == 'nt' else 'clear')

def add_bean(connection):
    name = input("Enter the name of the bean: ")
    method = input("Enter the preparation method: ")
    rating = int(input("Enter your rating for this preparation method (0-100): "))
    main.add_bean(name, method, rating)

def view_all_beans(connection):
    beans = main.get_all_beans(connection)
    for bean in beans:
        print(f"- ID {bean[0]}: {bean[1]}")
    
def search_for_bean(connection):
    name = input("Enter the name of the bean you want to search for: ")
    beans = main.get_beans_by_name(connection, name)
    for bean in beans:
        print(f"- {bean[1]} ({bean[2]}) - {bean[3]}/100")

def get_best_prep(connection):
    name = input("Enter the name of the bean you want to find the best preparation method for: ")
    best_prep = main.get_best_prep(connection, name)
    print(f"The best preparation method for {name} is {best_prep[2]}.")

def delete_bean(connection):
    name = input("Enter the name of the bean you want to delete: ")
    bean_id = input("Enter the ID of the bean you want to delete: ")
    main.delete_bean(connection, name, bean_id)






menu()