# Inspired by one of Uncle Bob's TDD Kata

# Write a function that generates factors for a given number.

# The function takes an integer as parameter and returns a list of integers (ObjC: array of NSNumbers representing integers). That list contains the prime factors in numerical sequence.


def prime_factors(n):
    divider = 2
    result = []
    while (divider * divider) <= n:
        if n % divider:
            divider += 1
        else:
            n //= divider
            result.append(divider)
    if n > 1:
        result.append(n)
    return result
