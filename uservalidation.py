"""
    Description of the code:
    1. Prompt new user to enter their details.
    2. Use a List as a database to store credidentials. 
       Note: You can use a real database (sqlite or Postgresql) to store the data or even a text file when you learn File Handling in Python.
    3. I've used symbols to make the user not to read the password they had entered earlier but they can scroll back.
    4. Try iterating through the List db to validate user password.
    FINALLY: You can think of multiple ways of writting this program and still get an output. That's what makes someone a problem solver.
"""
# Register
print("Hello new user, register below.\n")

username = input("Enter Username: ")
password = input("Enter password: ")

# store the pwd and usr name in a list db using 'append'
user_database = []
user_database.append(username)
user_database.append(password)

for symbol in "*********************************************************":
    print(symbol*2)

# Now do validation
enterpass = input(f"Welcome {user_database[0]} please re-enter your password to confirm it's you: ")

while enterpass != user_database[1]:
	enterpass = input(f"Password for user {user_database[0]} is incorrect, Try again ? ")

print("Correct. You're logged in now")