def only_duplicates(st):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    result = ''.join([char for char in text if frequency[char] > 1])
    
    return result
