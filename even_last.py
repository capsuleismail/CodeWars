# Given a sequence of integers, return the sum of all the integers that have an even index (odd index in COBOL), multiplied by the integer at the last index.
# Indices in sequence start from 0.
# If the sequence is empty, you should return 0.
def even_last(numbers):

    result = 0
    while numbers:
        for i in range(len(numbers)):
            if i % 2 == 0:
                result += numbers[i]*numbers[-1]
        return result
    else: return 0
