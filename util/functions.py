# Function to get password and modify it
def get_password():
    password = input("Create password: ")

    modified_password = ""

    for letter in password:
        if letter == 'i':
            modified_password += '!'
        elif letter == 'a':
            modified_password += '@'
        elif letter == 'm':
            modified_password += 'M'
        elif letter == 'B':
            modified_password += '8'
        elif letter == 'o':
            modified_password += '.'
        else:
            modified_password += letter
    modified_password += 'q*s'

    return modified_password
