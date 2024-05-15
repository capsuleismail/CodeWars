def remove_smallest(numbers):
    if not numbers:
        return []
    minum = numbers.index(min(numbers))
    return numbers[:minum] + numbers[minum+1:]
