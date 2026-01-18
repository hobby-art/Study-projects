"""
This programm checks if a string (e.g. password) meets the requirements:
- at least 8 characters long;
- contain both uppercase and lowercase characters;
- has at least 1 digit.
"""

import re

# Regexes for equirements to match.
# A single regex could do this, but with separate rules it's easy to
# let the user know what exactly doesn't match.
has_len = re.compile(r"[a-zA-Z0-9]{8,}")
has_lower = re.compile(r"[a-z]")
has_upper = re.compile(r"[A-Z]")
has_digit = re.compile(r"[0-9]")


# Function to check if the password matches all the requirements.
def password_check(password):
    if not has_len.search(password):
        print("Password has to be at least 8 characters long.")
        return
    elif not has_lower.search(password):
        print("Password must have at least one lowercase character.")
        return
    elif not has_upper.search(password):
        print("Password must have at least one uppercase character.")
        return
    elif not has_digit.search(password):
        print("Password must have at least one digit.")
        return
    else:
        print("Acceptable password.")
        return True


user_password = "Password123"
password_check(user_password)
