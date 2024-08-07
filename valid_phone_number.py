import re
def valid_phone_number(phone_number):
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    
    if re.match(pattern, phone_number):
        return True
    else:
        return False
