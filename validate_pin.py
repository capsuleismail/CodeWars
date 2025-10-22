import re

def validate_pin(pin):
    count = 0
    while len(pin) == 6 or len(pin) == 4:
        txt = re.sub(r'[^0-9]', '', pin)
        
        return txt == pin
    return False
