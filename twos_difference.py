def twos_difference(lst): 
    
    result = []
    for i in lst:
        if i+2 in lst:
            result.append((i, i+2))
        if i-2 in lst:
            result.append((i-2, i))
            
    result = list(set(result))
    result.sort()
    return result
