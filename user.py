def login(database, username, password):
    for c in database:
        if c == username and database[c] == password:
            print("Welcome back, ",username)
            return username
        elif c == username and database[c] != password:
            print("Password invalid for current usename")
            return ""
        else:
            print("The user has not been found in the database")
            return ""
        
def register(database,username):
    for c in database:
        if c == username:
            print("Username alerady registered.")
            return ""
        print("Username has been registered")

def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_string = (username,"has donated ",donation_amt)
    print("Thank you for your donation!")
    return donation_string


def show_donations(donations):
    print("--- All Donations ---")
    if not donations:
        print("there are currently no donations")
    else:
        for i in donations:
            print(i)
