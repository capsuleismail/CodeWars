def high_and_low(numbers):
    result = list(map(int, numbers.split()))
    return f'{max(result)} {min(result)}'
