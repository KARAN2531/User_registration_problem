# User Registration problem

# UC1 - As a User need to enter a valid First Name
# Rule: First name starts with Cap and has minimum 3 characters

import re

def valid_first_name(first_name):
    if re.match(r"^[A-Z][a-z]{2,}$",first_name):
        return True
    else:
        return "Invalid: minimum 3 characters are required"

