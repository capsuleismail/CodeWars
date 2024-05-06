# Impliment the reverse function, which takes in input n and reverses it. For instance, reverse(123) should return 321.
# You should do this without converting the inputted number into a string.


def reverse(n):
    revert = 0
    while n > 0:
        revert = revert * 10 + n % 10
        print('Revert:', revert)
        n //= 10
        print('N:', n)

    return revert
