#Lesson_8_Conditionals 
#Combining If/elif/else statements

username = 'Joshua'
password = 'marieljoshua'
username = username.title()

username_Input = input("Username: ")
password_Input = input("Password: ")
username_Input = username_Input.title()

if username_Input == username:
    print("Username Valid!")
else:
    print("Username Incorrect!")

if password_Input == password:
    print("Password Valid!")
else:
    print("Password Incorrect!")

if username == username_Input and password == password_Input:
    print("You can now access your account!")
elif username == username_Input or password == password_Input:
    print("You need to make both correct not just one!")
else:
    print("Authenticating Both Have Failed")
