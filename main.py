import re

def email_validation(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False

# Test qilish
print(email_validation("example@gmail.com"))  # True
print(email_validation("example@gmail"))  # False
print(email_validation("example@gmail.com.uk"))  # False
print(email_validation("example@gmail.com.uk"))  # False
