def odd_or_even(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i]
    return 'odd' if result % 2 else 'even'
