def valid_parentheses(paren_str):
    count = 0
    for i in range(len(paren_str)):
        if paren_str[i] == "(":
            count += 1
        elif paren_str[i] == ")":
            count -= 1
            if count < 0:
                return False
    if count == 0:
        return True
    else:
        return False
