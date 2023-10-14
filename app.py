from homepage import show_homepage
from user import login, register, donate, show_donations
database = {"admin" : "password123"}
donations = []
authorized_user = ""
show_homepage()

if authorized_user == "" :
    print("You must be logged in to donate.")
else:
    print("Logged in as:",authorized_user)


while True:
    user_input = int(input("Choose an option: "))
    if user_input == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database,username,password)
    elif user_input == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = register(database,username)
        if authorized_user != "":
            database[username] = password
    elif user_input == 3:
        if authorized_user != "":
            print("You are not logged in")
            donation_string = donate(authorized_user)
            donations += donation_string
    elif user_input == 4:
        show_donations(donations)
    elif user_input == 5:
        print("Goodbye")
        break
    else:
        print("Enter a valid input")