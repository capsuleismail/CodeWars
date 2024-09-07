def rep_set(n):
    if n == 0:
        return []  
    else:
        previous = rep_set(n-1)
    
    return previous + [rep_set(n-1)]
