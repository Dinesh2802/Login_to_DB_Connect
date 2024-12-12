# dineshn2802@gmail.com
# Dinesh@2802

import psycopg2
#from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import re
import time
connection = psycopg2.connect(
     host = "localhost",
     user = "postgres",
     password = "Dinesh2802",
     database = "Login_DB"
)

#connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

mediator = connection.cursor()

user_name = input("Enter the Username:")

username_pattern = re.compile(r'[A-Za-z0-9_.+-]*@[A-Za-z]*.[A-Za-z]{2,3}')

if username_pattern.match(user_name):
    # Proceed with inserting into the database
    #mediator.execute("insert into login (user_name) values (%s)", (user_name,))
    print("Valid username")
else:
    print("Invalid username")

user_password = input("Enter the Password:")

password_pattern = re.compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;"\'<>,.?/-]).{8,16}$') #Correct, compiled regex pattern

if password_pattern.match(user_password):
    print("Valid Password")
else:
    print("Invalid Password")

if re.match(username_pattern,user_name) and re.match(password_pattern,user_password):
    # Proceed with inserting into the database
    #mediator.execute("insert into login (user_password) values (%s)", (user_password,))  
    mediator.execute("insert into login (user_name,user_password) values (%s, %s)", (user_name,user_password))
    print("Username and Password are Valid")
    print("Login successful!")
else:
    print("Username and Password are Invalid Password")


import time

user_name = username_pattern
user_password = password_pattern

# Maximum allowed attempts
MAX_ATTEMPTS = 3

# Counter for failed attempts
attempts = 0

# Function to handle the login
def login():
    global attempts
    while attempts < MAX_ATTEMPTS:
        # Get username and password from the user
        #user_name = username_pattern
        #user_password = password_pattern

        # Check if the credentials are correct
        if user_name == username_pattern and user_password == password_pattern:
            #print("Login successful!")
            break  # Exit the loop if login is successful
        else:
            attempts += 1
            print(f"Incorrect credentials. You have {MAX_ATTEMPTS - attempts} attempts left.")

            # If the user exceeds the max attempts, lock the login
            if attempts == MAX_ATTEMPTS:
                print("You have exceeded the maximum number of login attempts. Try again later.")
                # Optional: Add a delay before allowing the user to try again
                time.sleep(5)  # Lockout for 5 seconds (you can adjust this duration)
                attempts = 0  # Reset attempts for demonstration (or keep locked)

# Call the login function to start the login process
login()


mediator.execute("select * from login")

data = mediator.fetchall()

connection.commit()

for i in data:
    print(i)

connection.close()
