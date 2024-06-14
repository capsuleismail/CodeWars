def square_digits(num):
    digits = []
    while num > 0:
        digits.append((num % 10)**2)
        num //= 10
    digits.reverse() 
    return 0 if digits == [] else int(''.join(map(str,digits)))
