

class Menu:
    def main_menu():
        while True:
            try:
                    print("Welcome to Dice Roll Game!")
                    print("1. Register")
                    print("2. Log in")
                    print("3. Exit")

                    choice = int(input("Enter your choice: "))

                    if choice == 1:
                        break
                    if choice == 2:
                        Menu.login_menu()
                        break
                    if choice == 3:
                        print("Thank you for playing")
                        exit(0)
                    else:
                        print("Enter a valid input\n")
            
            except ValueError:
                print("Invalid choice\n")

    def login_menu():
        while True:
            try:
                print("Log in Menu")
                print("1. Start Game")
                print("2. View Leaderboard")
                print("3. Log out")

                choice = int(input("Enter choice: "))

                if choice == 1:
                    break
                    pass
                if choice == 2:
                    break
                    pass
                if choice == 3:
                    Menu.main_menu()
                    break
                else:
                    print("Enter a Valid Input\n")
            except ValueError:
                print("Invalid choice\n")

Menu.main_menu()
    


