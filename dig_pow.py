def dig_pow(n, p):
    result = []
    original_n = n
    while n:
        print((n%10)*p)
        result.append(n % 10)
        
        n //= 10
        
    result = result[::-1]
    total = sum(result[i] ** (p + i) for i in range(len(result)))
    
    if total % original_n == 0:
        return total // original_n
    else:
        return -1
