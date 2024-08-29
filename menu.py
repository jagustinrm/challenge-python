from zoo import Zoo

# Códigos ANSI para colores
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def show_menu():
    print(f"\n{GREEN}----- Zoo Management System -----{RESET}")
    print(f"{CYAN}1. Add an Animal{RESET}")
    print(f"{CYAN}2. Remove an Animal{RESET}")
    print(f"{CYAN}3. Show All Animals{RESET}")
    print(f"{CYAN}4. Show Animal Count{RESET}")
    print(f"{CYAN}5. Show Admission Price{RESET}")
    print(f"{CYAN}6. Compare Giraffe Height{RESET}")
    print(f"{CYAN}7. Show Crocodile's Favorite Food{RESET}")
    print(f"{CYAN}8. Show Giant Tortoise Age Category{RESET}")
    print(f"{RED}9. Exit{RESET}")

def create_zoo():
    print(f"\n{GREEN}----- Create Your Zoo -----{RESET}")
    name = input("Enter the zoo's name: ").strip()
    city = input("Enter the city where the zoo is located: ").strip()
    operating_hours = input("Enter the operating hours (e.g., 9 AM - 5 PM): ").strip()
    return Zoo(name, city, operating_hours)

def continue_or_exit():
    while True:
        choice = input(f"{YELLOW}Do you want to return to the menu? (yes/no): {RESET}").strip().lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            print("We hope to see you later. Goodbye!")
            return False
        else:
            print(f"{RED}Invalid choice. Please type 'yes' or 'no'.{RESET}")
