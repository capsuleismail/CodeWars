def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def relatively_prime(n, arr):
    return [num for num in arr if gcd(n, num) == 1]
