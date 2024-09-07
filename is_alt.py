def is_alt(s):
    vowels = list('aeiou')
    if s[0] in vowels:
        expected = True
    else:
        expected = False
    
    for letter in s:
        if letter in vowels:
            if not expected:
                return False
            expected = False
        else:
            if expected:
                return False
            expected = True
    return True
