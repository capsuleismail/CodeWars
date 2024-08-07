def persistence(n):
    if n < 10:
        return 0
    
    num_str = str(n)
    
    
    product = 1
    for digit in num_str:
        product = product * int(digit)
    
    return 1 + persistence(product)
