import random
import string

print("Hi there!")
firstname = input("Can I have your firstname: ")
lastname = input("Your lastname please: ")
email_id = input("Finally, your email address: ")
detail_list = []


def random_string(string_length = 5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def employee_password():
    generate_password = firstname[0:2] + lastname[-2:] + random_string(5)
    modified_password = generate_password.lower()
    detail_list.append(modified_password)
    return modified_password
