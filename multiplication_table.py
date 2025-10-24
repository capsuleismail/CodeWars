def multiplication_table(size):

    result = []
    
    for i in range(1, size+1):
        x = []
        for j in range(1, size+1):
            x.append(i*j)
        result.append(x)
    return result
