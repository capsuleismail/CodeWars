def even_fib(n):
    memo = {}

    def fib(k):
        if k in memo:
            return memo[k]
        if k <= 1:
            return k
        memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    evens = 0
    i = 0

    while True:
        value = fib(i)
        if value > n - 1:
            break
        if value % 2 == 0:
            evens += value
        i += 1

    return evens
