def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    
    x = 0
    y = 0
    
    for i in range(len(walk)):
        if walk[i] == 'n':
            y += 1
        elif walk[i] == 's':
            y -= 1
        elif walk[i] == 'e':
            x += 1
        elif walk[i] == 'w':
            x -= 1
            
    if x == 0 and y == 0:
        return True
    else:
        return False
