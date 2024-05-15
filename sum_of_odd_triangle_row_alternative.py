def sum_of_odd_triangle_row_alternative(n):
    start = n ** 2
    return sum(range(start, start + n * 2, 2))
