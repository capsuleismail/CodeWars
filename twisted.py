def compute_sum(n):

    total = 0
    factor = 1

    while factor <= n:
        lower = n % factor
        current = (n // factor) % 10
        higher = n // (factor * 10)

        total += higher * 45 * factor
        total += (current * (current - 1) // 2) * factor
        total += current * (lower + 1)

        factor *= 10

    return total
