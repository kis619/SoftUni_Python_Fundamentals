# Write a function that checks if a given password is valid. Password validations are:
# "	It should be 6 - 10 (inclusive) characters long
# "	It should consist only of letters and digits
# "	It should have at least 2 digits
# If a password is valid print "Password is valid".
# Otherwise, for every unfulfilled rule print a message:
# "	"Password must be between 6 and 10 characters"
# "	"Password must consist only of letters and digits"
# "	"Password must have at least 2 digits"

def password_validator(password):
    password_is_valid = True
    if not 6 <= len(password) <= 10:
        password_is_valid = False
        print("Password must be between 6 and 10 characters")
    for char in password:
        if ord(char) > 122 or 90 < ord(char) < 97 or 57 < ord(char) < 65 or ord(char) < 48:
            password_is_valid = False
            print("Password must consist only of letters and digits")
            break
    counter = 0
    for char in password:
        if 48 <= ord(char) <= 57:
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False
    if password_is_valid:
        print("Password is valid")



entered_password = input()

password_validator(entered_password)



