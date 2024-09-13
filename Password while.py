# Password while loop
# Name
name1 = input("What is your Name: ")
# Password
password = int(input(f"please choose your pasword {name1}: "))
#login
login = int(input(f"please enter your pasword {name1}: "))
while login != password:
    print("The password entered is incorrect.please try again. ")
    login = int(input(f"please enter your pasword {name1}: "))
    if login == password:
        print("The password is correct.you are logged in.")
