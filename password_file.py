import employee_file


def generate_password():
    print(f"\nYour generated password is {employee_file.employee_password()}\n")
    print("""
Select 1 to accept this password
Select 2 to discard this password (Note: If you select his option, you must create your own password to continue)\n""")
    while True:
        choice = input("Choice: ")
        if choice == "1":
            print("Great!, Below are your details: ")
            print(f"First Name: {employee_file.firstname}\n Last Name: {employee_file.lastname} \n Email address: "
                  f"{employee_file.email_id}\n")
            print(f"Password: {employee_file.employee_password()}\n")
            break
        elif choice == "2":
            while True:
                user_password = input("Please enter your desired password (Note password should be greater than or "
                                      "equal to 7 characters):  ")
                length_of_password = int(len(user_password))
                if length_of_password >= 7:
                    print("Excellent password")
                    print(f"First Name: {employee_file.firstname}\n Last Name: {employee_file.lastname} \n "
                          f"Email address: {employee_file.email_id}\n")
                    print(f" Your password is {user_password}")
                    break
                else:
                    print("Password length is not upto 7. Try again")
        else:
            print("Please enter a valid choice")
        break


generate_password()