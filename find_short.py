def find_short(s):
    result = [len(element) for element in s.split()]
    return min(result)
