def break_to_hide_reg_details():
    for symbol in "*********************************************************":
        print(symbol*2)

def register_user():
    username = input("Enter Username: ")
    password = input("Enter password: ")

    my_list_db = []
    my_list_db.append(username)
    my_list_db.append(password)

    break_to_hide_reg_details()

    enterpass = input(f"Welcome {my_list_db[0]} please re-enter your password to confirm it's you: ")

    if enterpass == my_list_db[1]:
        print("Correct. You're logged in now")

    else:
        while enterpass != my_list_db[1]:
            try:
                enterpass = input(f"Password for user {my_list_db[0]} is incorrect, Try again ? ")

            except:
                enterpass = input(f"Password for user {my_list_db[0]} is incorrect, Try again ? ")

            else:
                if enterpass in my_list_db:
                    print("Correct. You're logged in now")


def home():
    print("Hello new user, register below.\n")
    register_user()

home()