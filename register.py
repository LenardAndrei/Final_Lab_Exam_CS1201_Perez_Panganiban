import os


class Register:

    def register():

        if not os.path.exists("DB.txt"):
            file = open("DB.txt", "x")


        Register.username()



    def username():

        while True:
            name = input("Input your username: ")

            if not Register.validate_username(name):
                continue

    

            with open("DB.txt", "a") as file:
                file.write(name)


            file.close()

            exit(0)
            break





    def password():

        while True:
            password = input("Input your password: ")

            if len(password) < 8:
                print("input a password that is 8 characters or longer.")
                continue

        
            else:
                break








    def validate_username(name):

        result = True

        if len(name) < 4:
                print("input a name that is 4 characters or longer.")
                result = False

        return result

            

    
    def validate_password():
        pass





