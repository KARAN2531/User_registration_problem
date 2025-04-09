# User Registration problem

# UC1 - As a User need to enter a valid First Name
# Rule: First name starts with Cap and has minimum 3 characters

import re

def valid_first_name(first_name):
    if re.match(r"^[A-Z][a-z]{2,}$",first_name):
        return True
    else:
        return "Invalid: minimum 3 characters are required"


<<<<<<< HEAD
# UC2 - As a User need to enter a valid Last Name
# Rule: Last name starts with Cap and has minimum 3 characters

def valid_last_name(last_name):
    if re.match(r"^[A-Z][a-z]{2,}$", last_name):
        return True
    else:
        return "Invalid: minimum 3 characters are required"
=======
# UC3 - As a User need to enter a valid email
# Rule: Email has 3 mandatory parts (abc, bl & co) and 2 optional (xyz & in) with precise @ and . positions

def validate_email(email):
    if re.match(r"^[\w]+(\.[\w]+)?@[\w]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$", email):
        return True
    else:
        return "Invalid: Not a valid email ID"
    
>>>>>>> use_case_3
