def digital_root(n):
    digit = 0
    if n < 10:
        return n
    else:
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        return digital_root(digit_sum)
