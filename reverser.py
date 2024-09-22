def reverse_recursive(n, rev=0):
    if n == 0:
        return rev
    
    last_digit = n % 10
    rev = rev * 10 + last_digit
    
    return reverse_recursive(n // 10, rev)

def reverser(n):
    sign = 1 if n >= 0 else -1
    return sign * reverse_recursive(abs(n))
