
def powers(n):
    power = 1
    result = []
    while n > 0:
        if n & 1 == 1:  # I prefer more check if the last digit of the number is odd n%2==1 is lower
            result.append(power)
        n = int(n // 2)
        power = power * 2

    return result
