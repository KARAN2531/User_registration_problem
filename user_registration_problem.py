# User Registration problem

# UC1 - As a User need to enter a valid First Name
# Rule: First name starts with Cap and has minimum 3 characters

import re

def valid_first_name(first_name):
    if re.match(r"^[A-Z][a-z]{2,}$",first_name):
        return True
    else:
        return "Invalid: minimum 3 characters are required"


# UC2 - As a User need to enter a valid Last Name
# Rule: Last name starts with Cap and has minimum 3 characters

def valid_last_name(last_name):
    if re.match(r"^[A-Z][a-z]{2,}$", last_name):
        return True
    else:
        return "Invalid: minimum 3 characters are required"


# UC3 - As a User need to enter a valid email
# Rule: Email has 3 mandatory parts (abc, bl & co) and 2 optional (xyz & in) with precise @ and . positions

def validate_email(email):
    if re.match(r"^[\w]+(\.[\w]+)?@[\w]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$", email):
        return True
    else:
        return "Invalid: Not a valid email ID"

    
# UC4 - As a User need to follow pre-defined Mobile Format
# E.g. 91 9919819801 
# Country code follow by space and 10 digit number

def validate_mobile(mobile):
    pattern = r'^[0-9]{2}\s[0-9]{10}$'
    if re.match(pattern, mobile):
        return True
    else:
        return "Invalid: Mobile number must be in format '91 1234567890'"


# As a user needs to follow pre-defined Password rules.
# UC5 - Rule1:  Minimum 8 characters
# UC6 - Rule2:  Should have atleast 1 Uppercase
# UC7 - Rule3:  Should have atleast 1 numeric number in the password

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
    if re.match(pattern, password):
        return True
    else:
        return ("Invalid: Password must have at least 8 characters")
