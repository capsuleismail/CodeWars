def count_bits(n):
    if n == 0:
        return 0
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary

        n //= 2

    return binary.count('1')
