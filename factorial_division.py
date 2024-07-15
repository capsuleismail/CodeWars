def factorial_division(n, d):

    result = 1
    for i in range(d+1, n+1):
        result *= i
    return result
    
