def array_diff(a, b):
    if a == []:
        return []
    if b == []:
        return a
    
    for i in range(len(a)):
        if a[i] in b:
            temp = b.index(a[i])
            a[i] = None
        
    return list(filter(lambda x: x is not None, a))
